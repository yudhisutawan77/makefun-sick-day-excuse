# The Funniest Sick-Day Excuse

[![make.fun](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![Rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/yudhisutawan77/makefun-sick-day-excuse/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![Reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/yudhisutawan77/makefun-sick-day-excuse/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

One line, under 200 characters, that someone could send to call in sick — the
funniest excuse that lands in one breath, and nothing else.

Entry for the [make.fun bounty](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
"The Funniest Sick-Day Excuse" (sponsor: Zero Five, pot $2, top 3 split the pool).

## The line

> I got stung by a bee while brushing my teeth and now my lip looks like it lost an argument with a balloon animal.

113 characters. A bee sting mid-toothbrush: half believable, fresh (no fever, no
dog, no dead grandmother), and the punch — the lip losing an argument with a
balloon animal — arrives on the last words, exactly how a real text to a boss
would read.

## How it works

`main.py` (Python stdlib only) writes the line to `$ENTRY_OUT`, handling it
both as a file path and as a directory (in which case it writes `entry.txt`
inside it).

```sh
ENTRY_OUT=/output/entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
