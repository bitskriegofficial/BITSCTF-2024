# maxxing
## Description

```
MogamBro claims to have created a bot so good that it can never lose at Tic-Tac-Toe, and in his ego, he probably didn't even make a win condition. Can you prove him wrong and get the flag by any means?
```
<details>
  <summary>HINT #1</summary>
  You may be able to win against the unbeatable bot, but you still need to assemble to flag because MogamBro refused to code it in. Or he did and just called something else on purpose...
</details>
<details>
  <summary>HINT #2</summary>
  There is a for loop that for some reason reads from an array of {1,1,1}, and keeps multiplying it by itself. Maybe if the array was something else that was already in / being constructed in the program, and all you had to do was change the values of 1 to ...
</details>

## Solution
We have a supposedly unbeatable tic-tac-toe bot, and playing against it once seems to confirm that we can never win (without any external help!). However the challenge description seems to hint that simply winning is not enough. Opening the binary in ghidra, we get

```c

undefined8 main(void)

{
  undefined8 uVar1;
  long in_FS_OFFSET;
  int local_20;
  int local_1c;
  int local_18;
  int local_14;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  for (local_18 = 0; local_18 < 3; local_18 = local_18 + 1) {
    for (local_14 = 0; local_14 < 3; local_14 = local_14 + 1) {
      (&board)[(long)local_18 * 3 + (long)local_14] = 0;
    }
  }
  makeBestMove();
  do {
    while( true ) {
      uVar1 = hasWinner(1);
      if ((int)uVar1 != 0) goto LAB_00102132;
      uVar1 = hasWinner(2);
      if ((int)uVar1 != 0) goto LAB_00102132;
      uVar1 = isBoardFull();
      if ((int)uVar1 != 0) goto LAB_00102132;
      printBoard();
      printf("Enter your move (row, column, 0 indexing): ");
      __isoc99_scanf("%d %d",&local_20,&local_1c);
      uVar1 = isValidMove(local_20,local_1c);
      if ((int)uVar1 != 0) break;
      puts("Invalid move! Try again.");
    }
    (&board)[(long)local_20 * 3 + (long)local_1c] = 2;
    uVar1 = hasWinner(2);
    if ((int)uVar1 == 0) {
      uVar1 = isBoardFull();
      if ((int)uVar1 != 0) {
        printBoard();
        puts("It\'s a draw!");
        goto LAB_00102132;
      }
    }
    else {
      printBoard();
      puts("You win!");
      flag = 1;
      syaaoksnqd();
    }
    makeBestMove();
    uVar1 = hasWinner(1);
    if ((int)uVar1 != 0) {
      printBoard();
      puts(&DAT_001030c8);
      goto LAB_00102132;
    }
    uVar1 = isBoardFull();
  } while ((int)uVar1 == 0);
  printBoard();
  puts("It\'s a draw!");
LAB_00102132:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
<br>
The code seems to be a tictactoe bot created using minimax algorithm to avoid losing to the player, and if in case the player wins calls a function syaaoksnqd(). 

```c
  if (flag != 0) {
    local_70 = 0x38303037;
    local_6c = 0;
    local_6b = 0x44313637;
    local_67 = 0;
    local_66 = 0x43304531;
    local_62 = 0;
    local_61 = 0x33303343;
    local_5d = 0;
    local_5c = 0x41413131;
    local_58 = 0;
    local_57 = 0x34304130;
    local_53 = 0;
    local_52 = 0x44354442;
    local_4e = 0;
    local_4d = 0x39413434;
    local_49 = 0;
    local_48 = 0x32363346;
    local_44 = 0;
    local_43 = 0x32393333;
    local_3f = 0;
    local_3e = 0x35363831;
    local_3a = 0;
    local_39 = 0x44394541;
    local_35 = 0;
    local_34 = 0x34443444;
    local_30 = 0;
    local_2f = 0x30463137;
    local_2b = 0;
    local_2a = 0x38393236;
    local_26 = 0;
    local_25 = 0x44463242;
    local_21 = 0;
    local_74 = 0x463439;
    sVar1 = strlen((char *)&local_70);
    sVar2 = strlen((char *)&local_6b);
    sVar3 = strlen((char *)&local_66);
    sVar4 = strlen((char *)&local_61);
    sVar5 = strlen((char *)&local_5c);
    sVar6 = strlen((char *)&local_57);
    sVar7 = strlen((char *)&local_52);
    sVar8 = strlen((char *)&local_4d);
    sVar9 = strlen((char *)&local_48);
    sVar10 = strlen((char *)&local_43);
    sVar11 = strlen((char *)&local_3e);
    sVar12 = strlen((char *)&local_39);
    sVar13 = strlen((char *)&local_34);
    sVar14 = strlen((char *)&local_2f);
    sVar15 = strlen((char *)&local_2a);
    sVar16 = strlen((char *)&local_25);
    sVar17 = strlen((char *)&local_74);
    __dest = (undefined2 *)
             malloc(sVar17 + sVar1 + sVar2 + sVar3 + sVar4 + sVar5 + sVar6 + sVar7 + sVar8 + sVar9 +
                             sVar10 + sVar11 + sVar12 + sVar13 + sVar14 + sVar15 + sVar16 + 3);
    *__dest = 0x7830;
    *(undefined *)(__dest + 1) = 0;
    strcat((char *)__dest,(char *)&local_70);
    strcat((char *)__dest,(char *)&local_6b);
    strcat((char *)__dest,(char *)&local_66);
    strcat((char *)__dest,(char *)&local_61);
    strcat((char *)__dest,(char *)&local_5c);
    strcat((char *)__dest,(char *)&local_57);
    strcat((char *)__dest,(char *)&local_52);
    strcat((char *)__dest,(char *)&local_4d);
    strcat((char *)__dest,(char *)&local_48);
    strcat((char *)__dest,(char *)&local_43);
    strcat((char *)__dest,(char *)&local_3e);
    strcat((char *)__dest,(char *)&local_39);
    strcat((char *)__dest,(char *)&local_34);
    strcat((char *)__dest,(char *)&local_2f);
    strcat((char *)__dest,(char *)&local_2a);
    strcat((char *)__dest,(char *)&local_25);
    strcat((char *)__dest,(char *)&local_74);
    for (local_bc = 0; local_bc < 3; local_bc = local_bc + 1) {
    }
    puts("It can\'t be...");
    printf("BITSCTF{n0t_th4T_eZ}");
  }
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
```
With some effort, we can trace back the original code as 
```c
char s0[] = "7008";
char s1[] = "761D";
char s2[] = "1E0C";
char s3[] = "C303";
char s4[] = "11AA";
char s5[] = "0A04";
char s6[] = "BD5D";
char s7[] = "44A9";
char s8[] = "F362";
char s9[] = "3392";
char s10[] = "1865";
char s11[] = "AE9D";
char s12[] = "D4D4";
char s13[] = "71F0";
char s14[] = "6298";
char s15[] = "B2FD";
char s16[] = "94F";

char *arr[] = {(char*)0x133, (char*)0x7E4E0C1, NULL};
size_t total_length = 2; 
        total_length += strlen(s0) + strlen(s1) + strlen(s2) + strlen(s3) +
                        strlen(s4) + strlen(s5) + strlen(s6) + strlen(s7) +
                        strlen(s8) + strlen(s9) + strlen(s10) + strlen(s11) +
                        strlen(s12) + strlen(s13) + strlen(s14) + strlen(s15) +
                        strlen(s16);

char *concatenated_str = (char *)malloc(total_length + 1);
strcpy(concatenated_str, "0x");

strcat(concatenated_str, s0);
strcat(concatenated_str, s1);
strcat(concatenated_str, s2);
strcat(concatenated_str, s3);
strcat(concatenated_str, s4);
strcat(concatenated_str, s5);
strcat(concatenated_str, s6);
strcat(concatenated_str, s7);
strcat(concatenated_str, s8);
strcat(concatenated_str, s9);
strcat(concatenated_str, s10);
strcat(concatenated_str, s11);
strcat(concatenated_str, s12);
strcat(concatenated_str, s13);
strcat(concatenated_str, s14);
strcat(concatenated_str, s15);
strcat(concatenated_str, s16);

arr[2] = concatenated_str;

for (int i = 0; i < 3; i++) {
    ans *= brr[i];
}

printf("It can't be...\n");
printf("BITSCTF{n0t_th4T_eZ}");
}
```
<br>
Ignoring the fake flag, we need to know that ghidra stores hex in reverse, then we get these three hex 0x133, 0x7E4E0C1 and 0x7008761D1E0CC30311AA0A04BD5D44A9F36233921865AE9DD4D471F06298B2FD94F, and instead of the array of {1,1,1}, we multiply these hexes to get 

```
0x424954534354467B77335F6E3333645F74305F73743472545F6C306F6B356D345878316E477D
```
which we can convert to text to get the flag. 



## Flag

```
BITSCTF{w3_n33d_t0_st4rT_l0ok5m4Xx1nG}
```

## Author
[**@arm44n**](https://github.com/arm44n)