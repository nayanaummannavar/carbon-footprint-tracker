async function describe() {
    const input = document.getElementById("inputBox").value;

    if (!input) {
        alert("Enter something!");
        return;
    }

    try {
        const res = await fetch("http://127.0.0.1:5000/describe", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ input: input })
        });

        const data = await res.json();
        document.getElementById("output").innerText = data.data;

    } catch (error) {
        console.error(error);
        alert("Error connecting to backend");
    }
}