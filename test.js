/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {

    let current = [...needle]
    
    //let current be a copy of the array queue
    
    let startFlag = false
    let index = 0
    
    for(let i = 0 ; i < haystack.length;i++){
        console.log(current[0])
        if (!startFlag&&haystack[i]==current[0]){
            startFlag = true
            index = i
            current.shift()
            console.log(current)
            console.log(current[0])
        }
        else if(startFlag&&haystack[i]==current[0]){

            current.shift()
            console.log(haystack[i])
            console.log(current)
            console.log(current[0])
            if(current.length===0){
                return index
            }
        else 
        {
            
            startFlag = false
            current = [...needle]
        }
        }
    }
    
    return -1
    
    //keep popping off the queue if the front of queue matches with letter
    
    //if queue lenght is 0 , then u win 
    
    
    };

    console.log(strStr('sadbutsad','sad'))
    