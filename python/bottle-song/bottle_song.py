
lyric_numbers = [
"no",
"One",
"Two",
"Three",
"Four",
"Five",
"Six",
"Seven",
"Eight",
"Nine",
"Ten"
]

def recite(start, take=1):
    lyric = []
    unit_bottle = "bottles"
    next_unit_bottle = "bottles"
    
    for i in range(start,  start-take,-1):

        if i == 2 :
            next_unit_bottle = "bottle"
        elif i == 1 :
            unit_bottle = "bottle"
            next_unit_bottle = "bottles"

        lyric.append(f"{lyric_numbers[i]} green {unit_bottle} hanging on the wall,")
        lyric.append(f"{lyric_numbers[i]} green {unit_bottle} hanging on the wall,")
        lyric.append(f"And if one green bottle should accidentally fall,")
        lyric.append(f"There'll be {lyric_numbers[i-1].lower()} green {next_unit_bottle} hanging on the wall.")
        lyric.append("")

    lyric.pop()
    return lyric
