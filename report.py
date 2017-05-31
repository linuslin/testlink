#!//usr/bin/python
# coding="utf-8"

import testlink
serverlink="http://52.178.182.252/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
devkey="4663fd5ffabbfb4b1b74c5bbba077bcd"
tls = testlink.TestlinkAPIClient(serverlink, devkey)
tls.about()
#tls = testlink.TestLinkHelper().connect(testlink.TestlinkAPIGeneric)
#print tls.getProjects()
#proj=getProjectByName('AutoTest')
#print tls.getProjectTestPlans(152)

proj_name="AutoTest"
testPlan_name='ATPlan'
testPlanID=tls.getTestPlanByName(proj_name, testPlan_name)[0]['id']
print 'testPlanID=%s'%testPlanID
tls.reportTCResult(testplanid=testPlanID, status='f', testcaseid='160' ,buildid='5', notes='some notes' , user='AT')



