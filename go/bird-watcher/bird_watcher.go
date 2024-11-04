package birdwatcher

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) int {

	total := 0

	for _, birdcount := range(birdsPerDay) {
		total = total + birdcount
	}
	return total
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) int {

	weeklytotal := 0

	for i := 7* (week -1); i <  7 * week; i++ {
		weeklytotal = weeklytotal + birdsPerDay[i]
	}
	return weeklytotal
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
func FixBirdCountLog(birdsPerDay []int) []int {

	for i := range birdsPerDay {
		if i % 2 == 0 {
			birdsPerDay[i] = birdsPerDay[i] + 1
		}
	}
	return birdsPerDay
}
