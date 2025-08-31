const API_URL = "https://task-manager-api-e6li.onrender.com"; // Replace with your deployed backend URL

async function fetchTasks() {
    const response = await fetch(API_URL);
    const tasks = await response.json();
    const taskList = document.getElementById("taskList");
    taskList.innerHTML = "";
    tasks.forEach(task => {
        const li = document.createElement("li");
        li.className = "list-group-item d-flex justify-content-between align-items-center";
        li.innerHTML = `
            <span>${task.title} - ${task.description}</span>
            <button class="btn btn-danger btn-sm" onclick="deleteTask(${task.id})">Delete</button>
        `;
        taskList.appendChild(li);
    });
}

async function addTask() {
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    if (!title) return alert("Title is required");

    await fetch(`${API_URL}?title=${encodeURIComponent(title)}&description=${encodeURIComponent(description)}`, {
        method: "POST"
    });
    document.getElementById("title").value = "";
    document.getElementById("description").value = "";
    fetchTasks();
}

async function deleteTask(id) {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    fetchTasks();
}

document.getElementById("addTaskBtn").addEventListener("click", addTask);

// Initial fetch
fetchTasks();
