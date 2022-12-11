package main

import (
    "syscall/js"
    "strconv"
)

var Count = 0

func add(this js.Value, i []js.Value) interface{} {
	value1 := strconv.Itoa(1)
    value2 := strconv.Itoa(Count)
    
    int1, _ := strconv.Atoi(value1)
    int2, _ := strconv.Atoi(value2)

    js.Global().Set("output", int2+int1)
    Count = int1 + int2
    println(Count)
    document := js.Global().Get("document")
	    document.Call("getElementById", "int").Set("innerHTML", Count)
    return Count
}

func subtract(this js.Value, i []js.Value) interface{} {
    value1 := strconv.Itoa(1)
    value2 := strconv.Itoa(Count)
    
    int1, _ := strconv.Atoi(value1)
    int2, _ := strconv.Atoi(value2)
    js.Global().Set("output", int2-int1)
    Count = int2 - int1
    println(Count)
    document := js.Global().Get("document")
	    document.Call("getElementById", "int").Set("innerHTML", Count)
    return Count
}

func reset(this js.Value, i []js.Value) interface{} {
    Count = 0
    js.Global().Set("output", Count)
    println(Count)
    document := js.Global().Get("document")
	    document.Call("getElementById", "int").Set("innerHTML", Count)
    return Count
}

func registerCallbacks() {
    js.Global().Set("add", js.FuncOf(add))
    js.Global().Set("subtract", js.FuncOf(subtract))
    js.Global().Set("reset", js.FuncOf(reset))
}

func main() {
    c := make(chan struct{}, 0)

    println("WASM Go Initialized")
    // register functions
    registerCallbacks()
    <-c
}