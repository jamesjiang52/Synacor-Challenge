# Synacor Challenge

In this challenge, your job is to use this architecture spec to create a virtual machine capable of running the included binary.

## Architecture

* three storage regions
  * memory with `15`-bit address space storing `16`-bit values
  * eight registers
  * an unbounded stack which holds individual `16`-bit values
* all numbers are unsigned integers `0`..`32767` (`15`-bit)
* all math is modulo `32768`; `32758 + 15 => 5`

### Binary Format

* each number is stored as a `16`-bit little-endian pair (low byte, high byte)
* numbers `0`..`32767` mean a literal value
* numbers `32768`..`32775` instead mean registers `0`..`7`
* numbers `32776`..`65535` are invalid
* programs are loaded into memory starting at address `0`
* address `0` is the first `16`-bit value, address `1` is the second `16`-bit value, etc

### Execution

* After an operation is executed, the next instruction to read is immediately after the last argument of the current operation.  If a jump was performed, the next operation is instead the exact destination of the jump.
* Encountering a register as an operation argument should be taken as reading from the register or setting into the register as appropriate.
* The program "`9`,`32768`,`32769`,`4`,`19`,`32768`" occupies six memory addresses and should:
  * Store into register `0` the sum of `4` and the value contained in register `1`.
  * Output to the terminal the character with the ascii code contained in register `0`.

### Opcode listing
* halt: `0`
  * stop execution and terminate the program
* set: `1 a b`
  * set register `a` to the value of `b`
* push: `2 a`
  * push `a` onto the stack
* pop: `3 a`
  * remove the top element from the stack and write it into `a`; empty stack = error
* eq: `4 a b c`
  * set `a` to 1 if `b` is equal to `c`; set it to `0` otherwise
* gt: `5 a b c`
  * set `a` to 1 if `b` is greater than `c`; set it to `0` otherwise
* jmp: `6 a`
  * jump to `a`
* jt: `7 a b`
  * if `a` is nonzero, jump to `b`
* jf: `8 a b`
  * if `a` is zero, jump to `b`
* add: `9 a b c`
  * assign into `a` the sum of `b` and `c` (modulo `32768`)
* mult: `10 a b c`
  * store into `a` the product of `b` and `c` (modulo `32768`)
* mod: `11 a b c`
  * store into `a` the remainder of `b` divided by `c`
* and: `12 a b c`
  * stores into `a` the bitwise and of `b` and `c`
* or: `13 a b c`
  * stores into `a` the bitwise or of `b` and `c`
* not: `14 a b`
  * stores 15-bit bitwise inverse of `b` in `a`
* rmem: `15 a b`
  * read memory at address `b` and write it to `a`
* wmem: `16 a b`
  * write the value from `b` into memory at address `a`
* call: `17 a`
  * write the address of the next instruction to the stack and jump to `a`
* ret: `18`
  * remove the top element from the stack and jump to it; empty stack = halt
* out: `19 a`
  * write the character represented by ascii code `a` to the terminal
* in: `20 a`
  * read a character from the terminal and write its ascii code to `a`; it can be assumed that once input starts, it will continue until a newline is encountered; this means that you can safely read whole lines from the keyboard and trust that they will be fully read
* noop: `21`
  * no operation

## A Brief Introduction to Interdimensional Physics

Recent advances in interdimensional physics have produced fascinating predictions about the fundamentals of our universe! For example, interdimensional physics seems to predict that the universe is, at its root, a purely mathematical construct, and that all events are caused by the interactions between eight pockets of energy called "registers". Furthermore, it seems that while the lower registers primarily control mundane things like sound and light, the highest register (the so-called "eighth register") is used to control interdimensional events such as teleportation.

A hypothetical such teleportation device would need to have have exactly two destinations. One destination would be used when the eighth register is at its minimum energy level - this would be the default operation assuming the user has no way to control the eighth register. In this situation, the teleporter should send the user to a preconfigured safe location as a default.

The second destination, however, is predicted to require a very specific energy level in the eighth register. The teleporter must take great care to confirm that this energy level is exactly correct before teleporting its user! If it is even slightly off, the user would (probably) arrive at the correct location, but would briefly experience anomalies in the fabric of reality itself - this is, of course, not recommended. Any teleporter would need to test the energy level in the eighth register and abort teleportation if it is not exactly correct.

This required precision implies that the confirmation mechanism would be very computationally expensive. While this would likely not be an issue for large- scale teleporters, a hypothetical hand-held teleporter would take billions of years to compute the result and confirm that the eighth register is correct.

If you find yourself trapped in an alternate dimension with nothing but a hand-held teleporter, you will need to extract the confirmation algorithm, reimplement it on more powerful hardware, and optimize it. This should, at the very least, allow you to determine the value of the eighth register which would have been accepted by the teleporter's confirmation mechanism.

Then, set the eighth register to this value, activate the teleporter, and bypass the confirmation mechanism. If the eighth register is set correctly, no anomalies should be experienced, but beware - if it is set incorrectly, the now-bypassed confirmation mechanism will not protect you!

## Adventurer's Journal

**Day 1:** We have reached what seems to be the final in a series of puzzles guarding an ancient treasure. I suspect most adventurers give up long before this point, but we're so close! We must press on!

**Day 1:** P.S.: It's a good thing the island is tropical. We should have food for weeks!

**Day 2:** The vault appears to be sealed by a mysterious force - the door won't budge an inch. We don't have the resources to blow it open, and I wouldn't risk damaging the contents even if we did. We'll have to figure out the lock mechanism.

**Day 3:** The door to the vault has a number carved into it. Each room leading up to the vault has more numbers or symbols embedded in mosaics in the floors. We even found a strange glass orb in the antechamber on a pedestal itself labeled with a number. What could they mean?

**Day 5:** We finally built up the courage to touch the strange orb in the antechamber. It flashes colors as we carry it from room to room, and sometimes the symbols in the rooms flash colors as well. It simply evaporates if we try to leave with it, but another appears on the pedestal in the antechamber shortly thereafter. It also seems to do this even when we return with it to the antechamber from the other rooms.

**Day 8:** When the orb is carried to the vault door, the numbers on the door flash black, and then the orb evaporates. Did we do something wrong? Doesn't the door like us? We also found a small hourglass near the door, endlessly running. Is it waiting for something?

**Day 13:** Some of my crew swear the orb actually gets heaver or lighter as they walk around with it. Is that even possible? They say that if they walk through certain rooms repeatedly, they feel it getting lighter and lighter, but it eventually just evaporates and a new one appears as usual.

**Day 21:** Now I can feel the orb changing weight as I walk around. It depends on the area - the change is very subtle in some places, but certainly more noticeable in others, especially when I walk into a room with a larger number or out of a room marked `*`. Perhaps we can actually control the weight of this mysterious orb?

**Day 34:** One of the crewmembers was wandering the rooms today and claimed that the numbers on the door flashed white as he approached! He said the door still didn't open, but he noticed that the hourglass had run out and flashed black. When we went to check on it, it was still running like it always does. Perhaps he is going mad? If not, which do we need to appease: the door or the hourglass? Both?

**Day 55:** The fireflies are getting suspicious. One of them looked at me funny today and then flew off. I think I saw another one blinking a little faster than usual. Or was it a little slower? We are getting better at controlling the weight of the orb, and we think that's what the numbers are all about. The orb starts at the weight labeled on the pedestal, and goes down as we leave a room marked `-`, up as we leave a room marked `+`, and up even more as we leave a room marked `*`. Entering rooms with larger numbers has a greater effect.

**Day 89:** Every once in a great while, one of the crewmembers has the same story: that the door flashes white, the hourglass had already run out, it flashes black, and the orb evaporates. Are we too slow? We can't seem to find a way to make the orb's weight match what the door wants before the hourglass runs out. If only we could find a shorter route through the rooms...

**Day 144:** We are abandoning the mission. None of us can work out the solution to the puzzle. I will leave this journal here to help future adventurers, though I am not sure what help it will give. Good luck!



