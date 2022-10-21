global _start

  section .data
    msg: db "Hello, world!", 0xa ; define string in RAM
    len: equ $-msg ; define int in RAM

  section .text

  _start:
    mov eax, 4 ; syscall write()
    mov ebx, 1 ; file descriptor
    mov ecx, msg ; push string into CPU register
    mov edx, len ; push int into CPU register
    int 0x80 ; tell the kernel to run
    mov al, 1 ; syscall exit()
    int 0x80 ; tell the kernel to end


