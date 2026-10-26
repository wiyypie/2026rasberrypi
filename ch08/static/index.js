const result = document.getElementById("result");

document.getElementById("now").addEventListener("click", async () => {
    const response = await fetch("/api/now");
    const data = await response.json();

    if (data.error) {
        result.textContent = data.error;
        return;
    }

    result.textContent =
        `온도: ${data.temperature}°C\n습도: ${data.humidity}%`;
});

document.getElementById("record").addEventListener("click", async () => {
    const response = await fetch("/api/record");
    const data = await response.json();

    result.textContent = data.map(row =>
        `${row.created_at} | 온도: ${row.temperature}°C | 습도: ${row.humidity}%`
    ).join("\n") || "저장된 기록 없음";
});
