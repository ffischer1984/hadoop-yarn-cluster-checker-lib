=Readme
* here a some xml-files for unit-tests
* ENDPOINT: /ws/v1/cluster/apps
* empty_cluster.xml: 
  * there are no running jobs
  * there should be no hits for the term "<state>RUN"
* running_app.xml: 
  * a job/application with name Zeppelin is running on the cluster
  * search for "<state>RUN" should find sth


