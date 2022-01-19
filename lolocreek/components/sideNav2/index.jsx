import { useState } from 'react';
import Image from 'next/image';
import cx from "classnames";

// components
import ImageBtn from 'components/imageBtn';

// styles
import StyleCSS from "./style.module.css";

// icons
import CompanyIcon from "icons/company.png";
import DiggerIcon from 'icons/digger.png';
import ForwardIcon from 'icons/forward.png';
import BackwardIcon from 'icons/backward.png';


const Index = () => {
  const [isOpen, setIsOpen] = useState(false)

  const toggleOpen = () => {
    let isOpenClone = isOpen
    setIsOpen(!isOpenClone)
  }

  const style = () => {
    if (isOpen) {
      return cx('grid col-span-5', StyleCSS.expanded)
    } else {
      return 'grid grid-cols-1 justify-items-center'
    }
  }

  const showNavWords = () => {
    if (isOpen) {
      return "inline-block"
    } else {
      return "hidden"
    }
  }

  return (
    <div className={cx(StyleCSS.main, 'md:hidden', style())}>
     
      <div className='col-span-6'>
        <table>
          <tbody>
            <tr className='flex place-items-center'>
              <td>
                <ImageBtn
                  img={CompanyIcon}
                  alt="About Us"
                  width={50}
                  height={50}
                />
              </td>
              <td className={showNavWords()}>About Us</td>
            </tr>
            <tr className='flex place-items-center'>
              <td>
                <ImageBtn
                  img={DiggerIcon}
                  alt="Services"
                  width={50}
                  height={50}
                />
              </td>
              <td className={showNavWords()}>Services</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div className='col-span-6 justify-self-end'>
        {
          isOpen ?
            <Image
              src={ForwardIcon}
              onClick={toggleOpen}
              width={50}
              height={50}
            />
            :
            <Image
              src={BackwardIcon}
              onClick={toggleOpen}
              width={50}
              height={50}
            />
        }
      </div>
    </div>
  );
}

export default Index;