
.text
main:
addi $2,$0,5 
syscall
add $3,$0,$2 #primeiro numero
addi $2,$0,5 #segundo numero
syscall
addi $10,$0,2
add $5,$3,$2
div $5,$10
mflo $6
add $4,$0,$6
addi $2,$0,1
syscall
addi $4,$0,44
addi $2,$0,11
syscall
mfhi $7
addi $20,$0,10
mul $8,$7,$20 
div $8,$10
mflo $9
add $4,$0,$9
addi $2,$0,1
syscall