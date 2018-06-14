### Power State

Simple utility that will write zero to the `cpu_dma_latency` interface to force low latency power state, and push the processor out of a deep sleep state.

note: this is only a big hammer approach for testing.

In grub set the following on boot to set a max cstate and set the intel_idle driver:

```
processor.max_cstate=1 intel_idle.max_cstate=1
``` 