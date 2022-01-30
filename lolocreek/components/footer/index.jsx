import Image from 'next/image';
import Link from 'next/link';

// components
import { Modal, Button } from 'components';
import { data } from 'datafiles/companyData';

// images
import { LogoBlack, LogoWhite } from 'images';

const Index = () => {

    const modalContent = () => {
        console.log(data);
        return (
            <div className='text-black grid md:grid-cols-2 p-3'>
                <div className='md:w-80 place-self-center'>
                    <Image
                        src={LogoWhite}
                        alt='logo'
                    />
                </div>
                <div>
                    <div className='mt-5 text-center'>
                        <p className='font-bold'>Phone Number:</p>
                        <p>{data.phoneNum.cell}</p>
                        <p className="font-bold mt-3">Email Address:</p>
                        <p>{data.email}</p>
                        <p className="font-bold mt-3">Address:</p>
                        <p>{data.address}</p>
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
                <p>{data.phoneNum.cell}</p>
                <p>{data.email}</p>
                <p>{data.address}</p>
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