# ASLR Test
This program will create the amount of child processes you provided in the args, and then log each child process's heap and stack address to one file.

This program's purpose is to test [ASLR(address space layout randomization)](https://en.wikipedia.org/wiki/Address_space_layout_randomization).

```
./main <number of child processes>
```

You can get the data of executing 25, 50, 100 child processes, and then run the entropy_calc.py to get the graph.