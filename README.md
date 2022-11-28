this is a place for me to play around/learn about using c/c++ from python.

## results

starting at 0 and incrementing a bunch of times:

* python: 66.35344479899504
* c dll: 1.1295300799974939

doing the above twice, once each in two threads:

* python: 141.43267440299678
* cpp dll: 1.350391801999649

## usage

to run the experiment, use the following.  `results.txt` will be written to the working directory.

```bash
make
```

## resources

* https://stackoverflow.com/questions/64478880/how-to-pass-this-numpy-array-to-c-with-ctypes
* https://stackoverflow.com/questions/5862915/passing-numpy-arrays-to-a-c-function-for-input-and-output
* https://stackoverflow.com/questions/5081875/ctypes-beginner
* https://stackoverflow.com/questions/145270/calling-c-c-from-python
* https://www.youtube.com/watch?v=YtiPCPtmZrs&list=LL&index=6&ab_channel=MikeShah
* https://github.com/cmaureir/unleash_cpp
