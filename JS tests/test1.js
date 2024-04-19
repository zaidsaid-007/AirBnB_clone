function average(){
    let Report = document.getElementById("Report")
    let subject = ["Math","Eng","Kiswahili","Science","Computer"]
    let marks =0
    for(let i=0;i<5;i++){
        marks = marks + parseInt(prompt("Enter the marks of "+subject[i]))
    }

    let studentsName = []
    num=studentsName.length;
    function getName(){
        let name = prompt("Enter your name")
        return name.trim()
    }
// while(num<5){
//     let name = prompt("Enter your name")
//     studentsName.push(name.trim())
//     num++
//     studentsName.push(name);
// }


    let mean = marks/5
    alert("The average marks of "+ studentsName + "is" + mean)


Report.onclick = average();

}

    

