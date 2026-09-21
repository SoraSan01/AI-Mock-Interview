function Home(){

    return(

        <div className="grid grid-cols-2 ">
            {/*Hero section*/}
            <div className="bg-white">
                   <div className="flex flex-row w-80 border
                        p-1  border-gray-200 rounded-2xl">
                    <div className="flex-none px-1">
                        <ul className="list-disc list-inside ">
                            <li className="text-purple-800"></li>
                        </ul>
                    </div>

                    <div className="flex-1">
                        Voice-to-Voice AI Interview Practice
                    </div>
        </div>
            </div>
            {/*AI voice interface*/}
            <div>
                  AI VOICE OVERVIEW
            </div>

        </div>
    )
}
export default Home;