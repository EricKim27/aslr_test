# ASLR Test
This program will create the amount of child processes you provided in the args, and then log each child process's heap and stack address to one file.

This program's purpose is to test [ASLR(address space layout randomization)](https://en.wikipedia.org/wiki/Address_space_layout_randomization).

```
./main <number of child processes>
```

you can Make this by running make, and then run the following command to draw a graph.

```
make plot
```