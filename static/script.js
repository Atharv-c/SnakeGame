async function play(choice){

    const response = await fetch("/play/" + choice);

    const data = await response.json();

    document.getElementById("user").innerHTML =
    "You Chose : " + data.user;

    document.getElementById("computer").innerHTML =
    "Computer Chose : " + data.computer;

    document.getElementById("result").innerHTML =
    data.result;

}
