# Logging Core Module version 1.Y.Z

Since we changed the logging architecture (v1.4.0), we forgot to remove toleration in the fluentd
StatefulSet. This setting allows fluentd to run on master nodes.

## Changelog

- Remove fluentd StatefulSet tolerations.
- Reduced Cerebro requests
- Changed Kibana rolling strategy to Recreate and removing kibana cpu limits

## Upgrade path

To upgrade this core module from `v1.6.0` to `v1.Y.Z`, you need to download this new version, then apply the
`kustomize` projects. No further action is required.

```bash
kustomize build katalog/fluentd | kubectl apply -f -
```
