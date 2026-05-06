// ------------------ DESCRIBE ------------------
async function describe() {
    console.log("Describe clicked");

    const input = document.getElementById("inputBox").value;

    if (!input) {
        alert("Please enter an activity");
        return;
    }

    document.getElementById("output").innerHTML = "⏳ Processing...";

    try {
        const res = await fetch("http://127.0.0.1:5000/describe", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ input: input })
        });

        const data = await res.json();
        console.log("Response:", data);

        document.getElementById("output").innerHTML = `
            <h3 style="color:#27ae60;"> Description</h3>
            <div>${data.data}</div>
        `;

    } catch (error) {
        console.error("ERROR:", error);
        document.getElementById("output").innerText = "❌ Error fetching data";
    }
}


// ------------------ RECOMMEND ------------------
async function recommend() {
    console.log("Recommend clicked");

    const input = document.getElementById("inputBox").value;

    if (!input) {
        alert("Please enter an activity");
        return;
    }

    document.getElementById("output").innerHTML = "⏳ Processing...";

    try {
        const res = await fetch("http://127.0.0.1:5000/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ input: input })
        });

        const data = await res.json();
        console.log("Response:", data);

        document.getElementById("output").innerHTML = `
            <h3 style="color:#27ae60;"> Recommendations</h3>
            <div>${data.data}</div>
        `;

    } catch (error) {
        console.error("ERROR:", error);
        document.getElementById("output").innerText = "❌ Error fetching data";
    }
}


// ------------------ GENERATE REPORT ------------------
async function generateReport() {
    console.log("Report clicked");

    const input = document.getElementById("inputBox").value;

    if (!input) {
        alert("Please enter an activity");
        return;
    }

    document.getElementById("output").innerHTML = "⏳ Generating report...";

    try {
        const res = await fetch("http://127.0.0.1:5000/generate-report", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ input: input })
        });

        const data = await res.json();
        console.log("Report Response:", data);

        document.getElementById("output").innerHTML = `
            <h3 style="color:#27ae60;">Carbon Footprint Report</h3>
            <div style="white-space: pre-line;">${data.data}</div>
        `;

    } catch (error) {
        console.error("ERROR:", error);
        document.getElementById("output").innerText = "❌ Error generating report";
    }
}