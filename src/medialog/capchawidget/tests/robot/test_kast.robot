# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s medialog.capchawidget -t test_kast.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src medialog.capchawidget.testing.MEDIALOG_CAPCHAWIDGET_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_kast.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Kast
  Given a logged-in site administrator
    and an add kast form
   When I type 'My Kast' into the title field
    and I submit the form
   Then a kast with the title 'My Kast' has been created

Scenario: As a site administrator I can view a Kast
  Given a logged-in site administrator
    and a kast 'My Kast'
   When I go to the kast view
   Then I can see the kast title 'My Kast'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add kast form
  Go To  ${PLONE_URL}/++add++Kast

a kast 'My Kast'
  Create content  type=Kast  id=my-kast  title=My Kast


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the kast view
  Go To  ${PLONE_URL}/my-kast
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a kast with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the kast title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
