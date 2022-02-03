import Image from 'next/image';
import Link from 'next/link';
import cx from "classnames";

// components
import { Modal, Button } from 'components';
import { data } from 'datafiles/companyData';

// images
import { LogoBlack, LogoWhite } from 'images';

const Index = () => {

    const modalContent = () => {
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
                        <a href={'tel:' + data.phoneNum.cellSimplified}><p className={cx('text-2xl font-cinzel md:text-4xl border-2 rounded-lg shadow-lg md:rounded-none md:shadow-none md:border-none md:hover:text-blue-500')}> {data.phoneNum.cell}</p></a>
                        <p className="font-bold mt-3">Email Address:</p>
                        <a href={'mailto:' + data.email}><p className='text-md font-bree md:text-lg border-2 rounded-lg shadow-lg md:rounded-none md:shadow-none md:border-none md:hover:text-blue-500'>{data.email}</p></a>
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
                            url: '/contact_us'
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
                    <li className='cursor-pointer'><Modal
                        btnText="Information"
                        modal={modalContent()}
                    /></li>
                </ul>
            </div>
            <div className='hidden md:flex flex-col place-self-center text-center'>
                <a href={'tel:' + data.phoneNum.cellSimplified}><p className={cx('text-2xl font-cinzel md:text-4xl border-2 rounded-lg shadow-lg md:rounded-none md:shadow-none md:border-none md:hover:text-blue-500')}> {data.phoneNum.cell}</p></a>
                <a href={'mailto:' + data.email}><p className='text-md font-bree md:text-lg border-2 rounded-lg shadow-lg md:rounded-none md:shadow-none md:border-none md:hover:text-blue-500'>{data.email}</p></a>
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