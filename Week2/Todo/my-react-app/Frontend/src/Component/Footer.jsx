function Footer() {
    return (
        <footer className="border-t border-slate-200 bg-white">
            <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-2 px-5 py-6 text-sm text-slate-500 sm:flex-row">
                <p>
                    © {new Date().getFullYear()} TaskFlow. Built with React.
                </p>

                <p>
                    Small steps. Big progress. 💜
                </p>
            </div>
        </footer>
    );
}

export default Footer;