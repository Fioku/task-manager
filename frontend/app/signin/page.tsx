'use client';

import { FaGoogle } from "react-icons/fa6";

export default function SignInPage() {
    const handleGoogleSignIn = () => {
        window.location.href = "http://localhost:8000/accounts/google/login/";
    }

    return (
        <main className="flex min-h-screen flex-col items-center justify-center gap-15 p-24">
            <h1 className="text-4xl font-bold">Task Nory</h1>
            <div className="w-72 bg-gray-400 h-1 rounded-4xl" />
            <button onClick={handleGoogleSignIn}
            className="flex items-center gap-2 rounded bg-white/90 px-4 py-2 text-black transition scale-100 hover:scale-105 shadow-black shadow-2xl cursor-pointer">
                <FaGoogle size={24} />
                <span>Sign in with Google</span>
            </button>
        </main>
    );
}