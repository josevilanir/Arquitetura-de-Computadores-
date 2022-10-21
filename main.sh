clear
nasm -f elf main.s
ld -m elf_i386 main.o -o compiled
./compiled
rm main.o compiled