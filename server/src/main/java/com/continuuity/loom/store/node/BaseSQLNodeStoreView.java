package com.continuuity.loom.store.node;

import com.continuuity.loom.cluster.Node;
import com.continuuity.loom.store.DBConnectionPool;
import com.continuuity.loom.store.DBPut;
import com.continuuity.loom.store.DBQueryExecutor;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Set;

/**
 * Base abstract class for {@link NodeStoreView} using a SQL database as the persistent store.
 */
public abstract class BaseSQLNodeStoreView implements NodeStoreView {
  private final DBConnectionPool dbConnectionPool;
  private final DBQueryExecutor dbQueryExecutor;

  BaseSQLNodeStoreView(DBConnectionPool dbConnectionPool, DBQueryExecutor dbQueryExecutor) {
    this.dbConnectionPool = dbConnectionPool;
    this.dbQueryExecutor = dbQueryExecutor;
  }

  abstract PreparedStatement getSelectAllNodesStatement(Connection conn) throws SQLException;

  abstract PreparedStatement getSelectNodeStatement(Connection conn, String id) throws SQLException;

  abstract PreparedStatement getDeleteNodeStatement(Connection conn, String id) throws SQLException;

  abstract PreparedStatement getNodeExistsStatement(Connection conn, String id) throws SQLException;

  abstract PreparedStatement getSetNodeStatement(Connection conn, Node node, ByteArrayInputStream nodeBytes) throws SQLException;

  abstract PreparedStatement getInsertNodeStatement(Connection conn, Node node, ByteArrayInputStream nodeBytes) throws SQLException;

  abstract boolean allowedToWrite(Node node);

  @Override
  public Set<Node> getClusterNodes(final String clusterId) throws IOException {
    return null;
  }

  @Override
  public Set<Node> getAllNodes() throws IOException {

    try {
      Connection conn = dbConnectionPool.getConnection();
      try {
        PreparedStatement statement = getSelectAllNodesStatement(conn);
        try {
          return dbQueryExecutor.getQuerySet(statement, Node.class);
        } finally {
          statement.close();
        }
      } finally {
        conn.close();
      }
    } catch (SQLException e) {
      throw new IOException("Exception getting all nodes");
    }
  }

  @Override
  public Node getNode(final String nodeId) throws IOException {
    try {
      Connection conn = dbConnectionPool.getConnection();
      try {
        PreparedStatement statement = getSelectNodeStatement(conn, nodeId);
        try {
          return dbQueryExecutor.getQueryItem(statement, Node.class);
        } finally {
          statement.close();
        }
      } finally {
        conn.close();
      }
    } catch (SQLException e) {
      throw new IOException("Exception getting nodes " + nodeId, e);
    }
  }

  @Override
  public void deleteNode(String nodeId) throws IOException {
    try {
      Connection conn = dbConnectionPool.getConnection();
      try {
        PreparedStatement statement = getDeleteNodeStatement(conn, nodeId);
        try {
          statement.executeUpdate();
        } finally {
          statement.close();
        }
      } finally {
        conn.close();
      }
    } catch (SQLException e) {
      throw new IOException("Exception deleting node " + nodeId, e);
    }
  }

  @Override
  public void writeNode(final Node node) throws IllegalAccessException, IOException {
    if (!allowedToWrite(node)) {
      throw new IllegalAccessException("Not allowed to write node " + node.getId());
    }

    try {
      Connection conn = dbConnectionPool.getConnection();
      try {
        ByteArrayInputStream nodeBytes = dbQueryExecutor.toByteStream(node, Node.class);
        DBPut nodePut = new NodeDBPut(node, nodeBytes);
        nodePut.executePut(conn);
      } finally {
        conn.close();
      }
    } catch (SQLException e) {
      throw new IOException("Exception writing node " + node.getId(), e);
    }
  }

  @Override
  public void writeNodes(Set<Node> nodes) throws IllegalAccessException, IOException {
    for (Node node : nodes) {
      writeNode(node);
    }
  }

  @Override
  public boolean nodeExists(String nodeId) throws IOException {

    try {
      Connection conn = dbConnectionPool.getConnection();
      try {
        PreparedStatement statement = getNodeExistsStatement(conn, nodeId);
        try {
          return dbQueryExecutor.hasResults(statement);
        } finally {
          statement.close();
        }
      } finally {
        conn.close();
      }
    } catch (SQLException e) {
      throw new IOException("Exception checking existence of node` " + nodeId, e);
    }
  }

  private class NodeDBPut extends DBPut {
    private final Node node;
    private final ByteArrayInputStream nodeBytes;

    private NodeDBPut(Node node, ByteArrayInputStream nodeBytes) {
      this.node = node;
      this.nodeBytes = nodeBytes;
    }

    @Override
    public PreparedStatement createUpdateStatement(Connection conn) throws SQLException {
      return getSetNodeStatement(conn, node, nodeBytes);
    }

    @Override
    public PreparedStatement createInsertStatement(Connection conn) throws SQLException {
      return getInsertNodeStatement(conn, node, nodeBytes);
    }
  }
}
