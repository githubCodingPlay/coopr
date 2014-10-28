/*
 * Copyright © 2012-2014 Cask Data, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package co.cask.coopr.shell.command;

import co.cask.coopr.provisioner.plugin.ResourceStatus;
import org.junit.Test;
import org.mockito.Mockito;

/**
 * {@link ListAutomatorTypeResourcesCommand} class test.
 */
public class ListAutomatorTypeResourcesCommandTest extends AbstractTest {

  private static final String INPUT =
    String.format("list resources from automator %s of type %s and status active", TEST_PLUGIN_TYPE,
                  TEST_RESOURCE_TYPE);

  @Test
  public void testExecute() throws Exception {
    CLI.execute(INPUT, System.out);
    Mockito.verify(PLUGIN_CLIENT).getAutomatorTypeResources(Mockito.eq(TEST_PLUGIN_TYPE),
                                                            Mockito.eq(TEST_RESOURCE_TYPE),
                                                            Mockito.eq(ResourceStatus.ACTIVE));
  }
}
