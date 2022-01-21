import DiggerIcon from 'icons/digger.png';
import ContactIcon from 'icons/contact.png';
import CompanyIcon from 'icons/company.png';
import HomeIcon from 'icons/home.png';


const data = [
    {
        title: 'Home',
        src: HomeIcon,
        width: 50,
        height: 50,
        alt:'home icon',
        url: '/'
    },
    {
        title: 'About Us',
        src: CompanyIcon,
        width: 50,
        height: 30,
        alt:'about us icon',
        url: 'about_us'
    },
    {
        title: 'Services',
        src: DiggerIcon,
        width: 50,
        height: 50,
        alt:'services icon',
        url: 'services'
    },
    {
        title: 'Contact Us',
        src: ContactIcon,
        width: 50,
        height: 50,
        alt:'contact us icon',
        url: 'contact_us'
    },
]

export default {data}
