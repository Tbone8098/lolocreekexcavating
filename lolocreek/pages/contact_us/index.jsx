import { Header, Footer } from 'components';

export default function Index() {
    return (
        <div className="flex flex-col h-screen">
            <div className='grid grid-col-12'>
                <div className='col-span-12'>
                    <Header />
                </div>
                <div className='col-span-10 col-start-2'>
                    <h2 className="text-2xl text-center">Send Us a Message</h2>
                    <form className='flex flex-col items-center' action="" method="post">
                        <input className='border w-fit text-center mb-3' type="text" name="fullname" id="fullname" placeholder='Fullname' />
                        <input className='border w-fit text-center mb-3' type="text" name="email" id="email" placeholder='Email'/>
                        <div className='w-100 mb-3'>
                        <textarea name="message" id="message" cols="" rows="10" className='border w-fit'></textarea>
                        </div>
                        <button className='border bg-orange-500 p-3'>Send</button>
                    </form>
                </div>
            </div>
            <div className='mt-auto'>
                <Footer />
            </div>
        </div>
    )
}
