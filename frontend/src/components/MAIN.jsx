import { useNavigate } from "react-router-dom"

function MainPage() {
    const navigate = useNavigate()

    const DinePonda = () => {
        navigate('/ponda')
    }

    const DineMargao = () => {
        navigate('/margao')
    }

    return (
        <div className=" w-screen h-screen bg-yellow-400 flex flex-col justify-center items-center">
            <img
                loading="lazy"
                src="/logo.png"
                alt="Chefs Bhojan logo"
                className="object-contain w-1/3 aspect-[1.2] "
            />
            <button onClick={DinePonda} className="flex items-center relative gap-2 px-10 py-5 mt-14 w-2/3 text-sm font-bold text-white bg-red-900 rounded-3xl shadow-[0px_1px_5px_rgba(0,0,0,0.25)] hover:scale-90 transition-transform">Dine in at Ponda
                <img className=" p-2 rounded-lg bg-white absolute right-5" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAASRJREFUSEvt1r8uBUEUx/HPLUR4A9EIGiW1hMJbEG+h9qf0Fhq19mr8eQOdQqESiYpEizvJrKw19s913SV2kslsZmbzPec358yZnpZaryWuXwdej0rcIvTQ6s6FvZNYwQSu8FhU9iuPX+PG/cG4F7/rzs3jErPxv2ssjQN8hO0C6JODP+HxHWbaAGdHkmePxeMOHCT/O1JfDC6O8xglu3FMzaXyfajgeknJU3KvB6MOChfNUOAbLDQoIJs4HgX4EDs1wU9YxMMowFM4xWoF/BlbOMnt+1YeZymwgWVMIx9cZ7Fq9XFfMC4rKqGarcW12umUcjRVncoECQZkxnbgRk+fTuqqNO+C64NCTd7VqedtmdxzCD20rMK9728CrjrTRuv/D/wG3ex3H0mWik0AAAAASUVORK5CYII=" />
            </button>
            <button onClick={DineMargao} className="flex items-center relative gap-2 px-10 py-5 mt-2 w-2/3 text-sm font-bold text-white bg-red-900 rounded-3xl shadow-[0px_1px_5px_rgba(0,0,0,0.25)] hover:scale-90 transition-transform">Dine in at Margao
                <img className=" p-2 rounded-lg bg-white absolute right-5" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAASRJREFUSEvt1r8uBUEUx/HPLUR4A9EIGiW1hMJbEG+h9qf0Fhq19mr8eQOdQqESiYpEizvJrKw19s913SV2kslsZmbzPec358yZnpZaryWuXwdej0rcIvTQ6s6FvZNYwQSu8FhU9iuPX+PG/cG4F7/rzs3jErPxv2ssjQN8hO0C6JODP+HxHWbaAGdHkmePxeMOHCT/O1JfDC6O8xglu3FMzaXyfajgeknJU3KvB6MOChfNUOAbLDQoIJs4HgX4EDs1wU9YxMMowFM4xWoF/BlbOMnt+1YeZymwgWVMIx9cZ7Fq9XFfMC4rKqGarcW12umUcjRVncoECQZkxnbgRk+fTuqqNO+C64NCTd7VqedtmdxzCD20rMK9728CrjrTRuv/D/wG3ex3H0mWik0AAAAASUVORK5CYII=" />
            </button>
        </div>
    )
}

export default MainPage