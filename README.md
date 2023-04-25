# Application-Vulnerabilities

These files each attack an application, each with different vulnerable methods such as gets() and strcpy(). A shellcode file was given in this collaboration that set the Linux user ID to 0 (root) and executed the “bin/sh” command to open a root shell. sol5.py circumvents data execution prevention by inserting the desire argument into an existing system call. sol6.py defeats address space layout randomization by prepending the payload with NOP instructions so the guessed address of the buffer nearly always lands in the NOP slide.
