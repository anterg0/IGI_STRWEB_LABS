document.addEventListener("DOMContentLoaded", function () {
    const styleToggle = document.getElementById("styleToggle");
    const stylePanel = document.getElementById("stylePanel");
    const fontSizeSelect = document.getElementById("fontSize");
    const textColorInput = document.getElementById("textColor");
    const bgColorInput = document.getElementById("bgColor");
    const resetButton = document.getElementById("resetButton");

    styleToggle.addEventListener("change", function () {
        stylePanel.style.display = styleToggle.checked ? "block" : "none";
    });

    fontSizeSelect.addEventListener("change", function () {
        document.body.style.fontSize = fontSizeSelect.value;
    });

    textColorInput.addEventListener("input", function () {
        document.body.style.color = textColorInput.value;
    });

    bgColorInput.addEventListener("input", function () {
        document.body.style.backgroundColor = bgColorInput.value;
    });

    resetButton.addEventListener("click", function () {
        document.body.style.fontSize = "";
        document.body.style.color = "";
        document.body.style.backgroundColor = "";

        fontSizeSelect.value = "18px";
        textColorInput.value = "#000000";
        bgColorInput.value = "#ffffff";
    });
});
