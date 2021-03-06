# Setting up Apache Spark in Kubernetes

# SPARK ON k8s TUTORIAL
[Check Youtube Video For Setting up Spark](https://www.youtube.com/watch?v=1CGGTMvy67c)

## Setting up Spark Using Helm 

* Go to `rbac/spark-rbac.yaml`  
  
_[RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) is Role based Access Control to define User Access Priviledges.
  K8s RBAC is Rest based and maps http verbs to the permissions_
  > A RoleBinding grants permissions within a specific namespace whereas a ClusterRoleBinding grants that access cluster-wide


* Go to `helm_values/sparkoperator_values.yaml` Read [more](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator).

### Exploring sparkoperator_values.yaml
 1. Spark createRole and createClusterRole is set `true`
 2. For now, we didn't enable monitoring using graffana or external service, so metrics & podMonitor is set to `false`
 3. __resources__ entirely depends system/docker capacity, change it accordingly
```
resources:
  limits:
    cpu: 2000m
    memory: 8000Mi
  requests:
    cpu: 200m
    memory: 100Mi
```
* Execute the Spark Operator helm file
```
$ helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator

$ helm install spark-operator spark-operator/spark-operator -n default -f sparkoperator_values.yaml --create-namespace
```


__Spark will create all pods inside _spark_ namespace only__

## Test 1
* Test Application by running `kubectl apply -f examples/spark/pi.yaml -n default` . Check the logs, a pi value will be logged if passed

## Test 2 
* Login to __minio__ and choose `test-files` bucket
* Upload any temporary file in the bucket
* Go to the director ../examples/spark
* Execute the spark wordcount job `kubectl apply -f examples/spark/wordcount.yaml -n default`
Spark should be able to read from minio which works like AWS s3