import { useState } from "react";

function Todo() {
    const [tasks, setTasks] = useState([]);
    const [title, setTitle] = useState("");
    const [filter, setFilter] = useState("all");

    /// Add Task Function /// 
    async function addTask(e) {
        e.preventDefault();

        const cleanTitle = title.trim();

        if (!cleanTitle) return;

        try {
            const response = await fetch(API_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    title: cleanTitle,
                }),
            });

            if (!response.ok) {
                throw new Error("Failed to create todo");
            }

            const savedTodo = await response.json();

            setTasks((prev) => [savedTodo, ...prev]);
            setTitle("");
        } catch (error) {
            console.error(error);
            alert("Task save nahi hua. Backend check karo.");
        }
    }

    function toggleTask(id) {
        setTasks((prev) =>
            prev.map((task) =>
                task.id === id
                    ? { ...task, completed: !task.completed }
                    : task
            )
        );
    }

    function deleteTask(id) {
        setTasks((prev) =>
            prev.filter((task) => task.id !== id)
        );
    }

    const filteredTasks = tasks.filter((task) => {
        if (filter === "active") return !task.completed;
        if (filter === "completed") return task.completed;
        return true;
    });

    const completedCount = tasks.filter(
        (task) => task.completed
    ).length;

    const remainingCount = tasks.length - completedCount;

    return (
        <main className="min-h-[75vh] bg-slate-50 px-4 py-12 sm:px-6">
            <div className="mx-auto max-w-2xl">
                {/* Heading */}
                <div className="mb-8">
                    <p className="mb-2 text-sm font-semibold uppercase tracking-widest text-indigo-600">
                        Your personal workspace
                    </p>

                    <h2 className="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
                        Get things done.
                    </h2>

                    <p className="mt-3 text-slate-500">
                        One task at a time. You’ve got this!
                    </p>
                </div>

                {/* Progress cards */}
                <div className="mb-6 grid grid-cols-3 gap-3">
                    <div className="rounded-2xl border border-slate-200 bg-white p-4">
                        <p className="text-sm text-slate-500">Total</p>
                        <p className="mt-1 text-2xl font-bold text-slate-900">
                            {tasks.length}
                        </p>
                    </div>

                    <div className="rounded-2xl border border-slate-200 bg-white p-4">
                        <p className="text-sm text-slate-500">Pending</p>
                        <p className="mt-1 text-2xl font-bold text-amber-600">
                            {remainingCount}
                        </p>
                    </div>

                    <div className="rounded-2xl border border-slate-200 bg-white p-4">
                        <p className="text-sm text-slate-500">Done</p>
                        <p className="mt-1 text-2xl font-bold text-emerald-600">
                            {completedCount}
                        </p>
                    </div>
                </div>

                {/* Add task form */}
                <form
                    onSubmit={addTask}
                    className="mb-6 flex gap-3 rounded-2xl border border-slate-200 bg-white p-3 shadow-sm"
                >
                    <input
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        placeholder="What needs to be done?"
                        maxLength={150}
                        className="min-w-0 flex-1 rounded-xl bg-transparent px-3 py-3 text-slate-900 outline-none placeholder:text-slate-400"
                    />

                    <button
                        type="submit"
                        className="rounded-xl bg-indigo-600 px-5 py-3 font-semibold text-white transition hover:bg-indigo-700 active:scale-95"
                    >
                        + Add
                    </button>
                </form>

                {/* Filters */}
                <div className="mb-4 flex flex-wrap gap-2">
                    {["all", "active", "completed"].map((item) => (
                        <button
                            key={item}
                            onClick={() => setFilter(item)}
                            className={`rounded-full px-4 py-2 text-sm font-medium capitalize transition ${filter === item
                                ? "bg-indigo-600 text-white"
                                : "border border-slate-200 bg-white text-slate-600 hover:bg-slate-100"
                                }`}
                        >
                            {item === "active" ? "Pending" : item}
                        </button>
                    ))}
                </div>

                {/* Task list */}
                <div className="space-y-3">
                    {filteredTasks.length === 0 ? (
                        <div className="rounded-2xl border border-dashed border-slate-300 bg-white px-5 py-12 text-center">
                            <div className="mb-3 text-4xl">
                                {tasks.length === 0 ? "📝" : "🎉"}
                            </div>

                            <h3 className="font-semibold text-slate-800">
                                {tasks.length === 0
                                    ? "No tasks yet"
                                    : "Nothing to show"}
                            </h3>

                            <p className="mt-2 text-sm text-slate-500">
                                {tasks.length === 0
                                    ? "Add your first task and get started."
                                    : "Try another filter to see your tasks."}
                            </p>
                        </div>
                    ) : (
                        filteredTasks.map((task) => (
                            <div
                                key={task.id}
                                className="group flex items-center gap-3 rounded-2xl border border-slate-200 bg-white p-4 shadow-sm transition hover:border-indigo-200"
                            >
                                <input
                                    type="checkbox"
                                    checked={task.completed}
                                    onChange={() => toggleTask(task.id)}
                                    aria-label={`Complete ${task.title}`}
                                    className="h-5 w-5 cursor-pointer accent-indigo-600"
                                />

                                <span
                                    className={`min-w-0 flex-1 break-words ${task.completed
                                        ? "text-slate-400 line-through"
                                        : "text-slate-700"
                                        }`}
                                >
                                    {task.title}
                                </span>

                                <button
                                    onClick={() => deleteTask(task.id)}
                                    aria-label={`Delete ${task.title}`}
                                    className="rounded-lg px-3 py-2 text-sm font-medium text-slate-400 transition hover:bg-red-50 hover:text-red-600"
                                >
                                    Delete
                                </button>
                            </div>
                        ))
                    )}
                </div>

                {tasks.length > 0 && (
                    <div className="mt-5 flex items-center justify-between text-sm text-slate-500">
                        <span>{remainingCount} task(s) remaining</span>

                        <button
                            onClick={() =>
                                setTasks((prev) =>
                                    prev.filter((task) => !task.completed)
                                )
                            }
                            disabled={completedCount === 0}
                            className="font-medium text-indigo-600 hover:text-indigo-800 disabled:cursor-not-allowed disabled:opacity-40"
                        >
                            Clear completed
                        </button>
                    </div>
                )}
            </div>
        </main>
    );
}

export default Todo;