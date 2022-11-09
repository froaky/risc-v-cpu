<hr>

## <B>Assembly Code</B>

<table width=100%>
<tr>
<td>

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
```

</td>
<td width=100%>

```
addi        r1,    r0,    420
addi        r2,    r1,    6
and         r3,    r2,    r1
or          r4,    r0,    r1
add         r5,    r6,    r7
storenoc
lw          r10,   0(r0)
sra         r9,    r1,    r2
beq         r3,    r4,    8
sub         r8,    r2,    r0
sw          r1,    4(r2)
sll         r5,    r0,    r0
beq         r10,   r0,    8
loadnoc     r1,    r2,    8
addi        r16,   r14,   210
loadnoc     r1,    r2,    8
```

</td>
</tr>
</table>

<br>
<hr>

## <B>Pipeline Diagram</B>

|   | |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|
|---|-|-|-|-|-|-|-|-|-|-|-|--|--|--|--|--|--|--|--|--|--|--|--|--|
| #1| |F|D|X|M|W| | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |
| #2| | |F|D|D|X|M|W| | | |  |  |  |  |  |  |  |  |  |  |  |  |  |
| #3| | | |F|F|D|D|X|M|W| |  |  |  |  |  |  |  |  |  |  |  |  |  |
| #4| | | | | |F|F|D|X|M|W|  |  |  |  |  |  |  |  |  |  |  |  |  |
| #5| | | | | | | |F|D|X|M|W |  |  |  |  |  |  |  |  |  |  |  |  |
| #6| | | | | | | | |F|D|X|M |W |  |  |  |  |  |  |  |  |  |  |  |
| #7| | | | | | | | | |F|D|X |M |W |  |  |  |  |  |  |  |  |  |  |
| #8| | | | | | | | | | |F|D |X |M |W |  |  |  |  |  |  |  |  |  |
| #9| | | | | | | | | | | |F |D |X |M |W |  |  |  |  |  |  |  |  |
|#10| | | | | | | | | | | |  |F |D |X |M |W |  |  |  |  |  |  |  |
|#11| | | | | | | | | | | |  |  |F |D |X |M |W |  |  |  |  |  |  |
|#12| | | | | | | | | | | |  |  |  |F |D |X |M |W |  |  |  |  |  |
|#13| | | | | | | | | | | |  |  |  |  |F |D |X |M |W |  |  |  |  |
|#14| | | | | | | | | | | |  |  |  |  |  |F |D |- |- |- |  |  |  |
|#15| | | | | | | | | | | |  |  |  |  |  |  |F |F |D |X |M |W |  |
|#16| | | | | | | | | | | |  |  |  |  |  |  |  |  |F |D |X |M |W |