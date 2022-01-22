import Image from 'next/image';

// components
import { Logo } from 'components';

// images
import { LogoBlack } from 'images';

const Index = () => {
    return (
        <div className="grid grid-cols-2 bg-black text-white mt-3">
            <div className="p-3">
                <ul>
                    <li>About Us</li>
                    <li>Services</li>
                    <li>Location</li>
                </ul>
            </div>
            <div className='p-2'>
                <Image
                src={LogoBlack}
                />
            </div>
        </div>
    );
}

export default Index;