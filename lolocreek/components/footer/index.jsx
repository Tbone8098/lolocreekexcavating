import Image from 'next/image';
import Link from 'next/link';

// components
import { Modal, Button } from 'components';

// images
import { LogoBlack, LogoWhite } from 'images';

const Index = () => {

    const modalContent = () => {
        return (
            <div className='text-black grid p-3'>
                <Image
                    src={LogoWhite}
                    alt='logo'
                />
                <div className='mt-5 text-center'>
                    <p className='font-bold'>Phone Number:</p>
                    <p>(123) 456-7890</p>
                    <p className="font-bold mt-3">Email Address:</p>
                    <p>brandon@lolocreekexcavating.com</p>
                    <p className="font-bold mt-3">Address:</p>
                    <p>1234 Somewhere in Montana Lane</p>
                </div>
                <Button
                    text="Contact Us"
                    attributes={{
                        display: 'block',
                        text: 'text-center text-white',
                        margin: 'mt-5'
                    }}
                    action={{
                        url:'/contact_us'
                    }}
                />
            </div>
        )
    }

    return (
        <div className="grid grid-cols-2 md:grid-cols-3 bg-black text-lolo-green mt-3">
            <div className="p-3 flex self-center">
                <ul>
                    <li>
                        <Link href='/about_us'>About Us</Link>
                    </li>
                    <li>
                        <Link href='/services'>Services</Link>
                    </li>
                    <li><Modal
                        btnText="Information"
                        modal={modalContent()}
                    /></li>
                </ul>
            </div>
            <div className='hidden md:flex flex-col place-self-center text-center'>
                <p>(406) 546-9948</p>
                <p>brandon@lolocreekexcavating.com</p>
                <p>Address is 6940 Mormon Creek Rd. Lolo MT 59847</p>
            </div>
            <div className='p-2 flex justify-end'>
                <Modal
                    btnText={
                        <Image
                            src={LogoBlack}
                            alt='lolo creek excavating logo'
                            width={200}
                            height={110}
                        />
                    }
                    modal={modalContent()}
                />
            </div>
        </div>
    );
}

export default Index;