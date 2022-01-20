import Header from 'components/header';
import Image from 'next/image';

// images
import Logo from 'images/lolocreeklogo.png';

export default function Index() {
    return (
        <div className='grid grid-cols-12'>
            <div className='col-span-12'>
                <Header />
            </div>
            <div className='col-span-10 col-start-2'>
                <h1 className='text-4xl text-center'>About Us</h1>
                <Image />
            </div>
        </div>
    )
}
