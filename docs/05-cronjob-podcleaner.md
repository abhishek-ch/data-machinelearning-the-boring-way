# Kubernetes: Pod Cleaner

_Cleaning all(any) Pods older than *n days_

Cleaning Pod is a pretty simple job by running the command `kubectl delete pod --field-selector=status.phase==Succeeded` but when the kubernetes cluster size is big and there are too many contributors, even deleting needs engineering!

## Pod Cleaner

A very simple utility to delete pods. Its designed as a cron job

#### Example
Delete all __Succeeded__ or __Failed__ pods @ 11:00 am everyday

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: podcleaner
  namespace: rwp
  labels:
    app: podcleaner
spec:
  schedule: "0 11 * * *"
  failedJobsHistoryLimit: 5
  successfulJobsHistoryLimit: 10
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
          - name: clean-pods
            imagePullPolicy: IfNotPresent
            image: buntha/podcleaner:0.2
            env:
              - name: MAX_DAYS
                value: "2"
              - name: POD_STATUS
                value: "Succeeded, Failed"
              - name: K8S_CONFIG
                value: "incluster"
              - name: NAMESPACE
                value: "default"
```

##### Parameters
* __MAX_DAYS__ : Number of Days since the pod state
* __POD_STATUS__: Succeeded, Failed, Running
* __NAMESPACE__: Pass the desired namespace or all
* __K8S_CONFIG__: incluster or anything


## Reference

This tiny project is fully inspired by https://github.com/dignajar/clean-pods but due to the kubernetes upgrade, the project is no more working, so I needed to change and create a new library.


# Service account for Kubernetes
Service account for the namespace demo with enoght permissions to list and delete pods.

Manifest service-account.yaml
```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: demo-user
  namespace: demo

---
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: demo-user-role
  namespace: demo
rules:
- apiGroups: [""]
  resources: ["pods","pods/exec","pods/log"]
  verbs: ["*"]

---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: demo-user
  namespace: demo
subjects:
- kind: ServiceAccount
  name: demo-user
  namespace: demo
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: demo-user-role 
```