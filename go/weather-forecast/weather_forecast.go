// Package weather is forcasted weather in Goblinocus.
package weather

// CurrentCondition is current weather.
var CurrentCondition string
// CurrentLocation is the forcast place.
var CurrentLocation string

// Forecast is .
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
