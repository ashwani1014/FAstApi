function Header() {
    return (
        <header className="border-b border-slate-200 bg-white">
            <div className="mx-auto flex max-w-6xl items-center justify-between px-5 py-5">
                <a href="/" className="flex items-center gap-3">
                    <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-indigo-600 text-xl font-bold text-white shadow-sm">
                        ✓
                    </div>

                    <div>
                        <h1 className="text-2xl font-bold text-slate-900">
                            Task<span className="text-indigo-600">Flow</span>
                        </h1>
                        <p className="text-xs text-indigo-500">
                            Organize your day
                        </p>
                    </div>
                </a>

                <span className="rounded-full bg-indigo-50 px-4 py-2 text-sm font-medium text-indigo-700">
                    Stay productive ✨
                </span>
            </div>
        </header>
    );
}

export default Header;