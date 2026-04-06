import './index.css'
import { useState, useEffect } from 'react';
import bgImage from './assets/download.gif';           // ← статичный фон сайта (можно заменить на любой JPG/PNG/GIF)
import earthGif from './assets/download (1).gif';       // ← гифка Земли (можно заменить на любую другую гифку)

function App() {
  // --- Состояния для управления интерфейсом ---
  const [menuVisible, setMenuVisible] = useState(false);  // видимость меню (false - скрыто, true - показано)
  const [languageOpen, setLanguageOpen] = useState(false); // открыто ли выпадающее окно языков
  const [activeSection, setActiveSection] = useState('home'); // активная секция (home, about, software, publications, work)
  const [showScrollButton, setShowScrollButton] = useState(false); // показывать ли кнопку "Вверх"
  const [textVisible, setTextVisible] = useState(false);  // для появления текста с задержкой

  // --- Эффект для появления меню через 4 секунды ---
  useEffect(() => {
    // setTimeout сработает один раз через 4000 миллисекунд (4 секунды)
    const timer = setTimeout(() => {
      setMenuVisible(true);  // меняем состояние на true - меню появляется
    }, 2000);  // ← ИЗМЕНЯЙТЕ это значение (в миллисекундах): 3000 = 3 сек, 5000 = 5 сек и т.д.

    // cleanup функция - очищает таймер, если компонент размонтируется до его срабатывания
    return () => clearTimeout(timer);
  }, []); // пустой массив зависимостей означает "выполнить только один раз при загрузке"

  // Эффект для появления текста через 4 секунды
useEffect(() => {
  const timer = setTimeout(() => {
    setTextVisible(true);
  }, 2000);  // ← через сколько секунд появляется текст
  return () => clearTimeout(timer);


    // добавляем слушатель события прокрутки
    window.addEventListener('scroll', handleScroll);
    // cleanup - удаляем слушатель при размонтировании
    return () => window.removeEventListener('scroll', handleScroll);
  }, []); // пустой массив - выполнить один раз

  // --- Функция плавной прокрутки к секции ---
  const scrollToSection = (sectionId) => {
    setActiveSection(sectionId);           // обновляем активную секцию для подсветки кнопки
    const element = document.getElementById(sectionId);  // находим элемент по ID
    if (element) {
      element.scrollIntoView({ 
        behavior: 'smooth',    // плавная прокрутка (можно 'auto' для мгновенной)
        block: 'start'         // выравнивание по верхнему краю ('center' или 'end')
      });
    }
  };

  // --- Функция прокрутки наверх ---
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,                  // прокручиваем к координате 0 (самый верх)
      behavior: 'smooth'      // плавная анимация
    });
  };

  // --- Данные для секций (каждая секция - это одна "страница" при скролле) ---
  // ИЗМЕНЯЙТЕ: добавляйте/удаляйте секции, меняйте заголовки, фото, описания
  const sections = [
    { 
      id: 'home', 
      title: 'Home', 
      image: earthGif,   
      image: bgImage,   
        // фото для секции (можно заменить на любую картинку)
      subtitle: 'Welcome to ASTRU',     // первая подпись
      description: 'We are an experimental research group at the University of Cologne and GSI Helmholtz Centre for Heavy Ion Research'     // вторая подпись
    },
    { 
      id: 'about', 
      title: 'About Us', 
      image: bgImage, 
      subtitle: 'About Us',
      description: 'Experimental Nuclear Astrophysics Group @University of Cologne & @GSI  Research Group at GSI Helmholtz Centre for Heavy Ion Research and the University of Cologne. The Experimental Nuclear Astrophysics Group at GSI and the University of Cologne is a research group that investigates the origins of elements through storage ring experiments.'
    },
    { id: 'team', 
      title: 'Team', 
      image: bgImage, 
      subtitle: 'Our Team', 
      description: 'Meet our researchers' 
    },
  
    { id: 'software', 
      title: 'Software & Tools', 
      image: bgImage, 
      subtitle: 'Наши разработки', 
      description: '...' 
    },
    { 
      id: 'software', 
      title: 'Software & Tools', 
      image: bgImage,
      subtitle: 'Наши разработки',
      description: 'Современные инструменты для бизнеса'
    },
    { 
      id: 'publications', 
      title: 'Publications', 
      image: bgImage, 
      subtitle: 'Публикации',
      description: 'Научные статьи и исследования'
    },
    { 
      id: 'work', 
      title: 'Work with Us', 
      image: earthGif, 
      image: bgImage,
      subtitle: 'Присоединяйтесь к команде',
      description: 'Открытые вакансии и сотрудничество'
    }
  ];

  // --- Доступные языки для выпадающего списка ---
  // ИЗМЕНЯЙТЕ: добавляйте/удаляйте языки по коду (ru, en, de, fr, es, it, zh, ja)
  const languages = [
    { code: 'ru', name: 'Русский' },
    { code: 'en', name: 'English' },
    { code: 'de', name: 'Deutsch' },
    { code: 'fr', name: 'Français' },
    { code: 'es', name: 'Español' },
    { code: 'it', name: 'Italiano' },
    { code: 'zh', name: '中文' }
  ];

  const [currentLanguage, setCurrentLanguage] = useState(languages[0]); // текущий выбранный язык

  return (
    <div className="min-h-screen bg-black overflow-x-hidden relative">
      {/* 
        ============================================================
        ФИКСИРОВАННАЯ ШАПКА (header) - всегда вверху, не скроллится
        ============================================================
      */}
      <header className="fixed top-0 left-0 w-full z-50 bg-black/80 backdrop-blur-md border-b border-white/10">
        <div className="container mx-auto px-6 py-4 flex items-center justify-between">
          
          {/* Левая часть шапки - оглавление (центр по факту) */}
          <div className="flex-1 flex justify-center">
            <div className="text-white text-xl font-bold tracking-wider">
              Experimental Nuclear Astrophysics Group @GSI    {/* ← СЮДА ВСТАВЬТЕ СВОЙ ТЕКСТ/ЛОГОТИП */}
            </div>
          </div>

          {/* Правая часть шапки - кнопки навигации и язык */}
          <div className="flex items-center gap-4">
            {/* Горизонтальное меню кнопок - появляется с анимацией через 4 секунды */}
            <div className={`flex gap-3 transition-all duration-700 transform ${
              menuVisible 
                ? 'opacity-100 translate-y-0'      // финальное состояние: видимо, на месте
                : 'opacity-0 -translate-y-10'      // начальное состояние: прозрачно, смещено вверх
            }`}>
              {/* Маппим массив кнопок */}
              {sections.map((section) => (
                <button
                  key={section.id}
                  onClick={() => scrollToSection(section.id)}
                  className={`px-4 py-2 rounded-lg text-sm font-medium transition-all duration-300 hover:scale-105 ${
                    activeSection === section.id
                      ? 'bg-purple-600 text-white shadow-lg shadow-purple-500/30'  // активная кнопка
                      : 'text-gray-300 hover:bg-white/10 hover:text-white'          // обычная кнопка
                  }`}
                >
                  {section.title}
                </button>
              ))}
            </div>

            {/* Выпадающий список языков */}
            <div className="relative">
              <button
                onClick={() => setLanguageOpen(!languageOpen)}  // клик - открыть/закрыть список
                className="px-4 py-2 rounded-lg bg-white/10 text-white hover:bg-white/20 transition-all duration-300 flex items-center gap-2"
              >
                🌐 {currentLanguage.name}   {/* показываем текущий язык */}
                <span className={`transform transition-transform duration-300 ${languageOpen ? 'rotate-180' : ''}`}>
                  ▼
                </span>
              </button>
              
              {/* Выпадающее окно со списком языков */}
              {languageOpen && (
                <div className="absolute right-0 mt-2 w-40 bg-gray-900/95 backdrop-blur-md rounded-lg shadow-xl border border-white/10 z-50 overflow-hidden animate-fadeInUp">
                  {languages.map((lang) => (
                    <button
                      key={lang.code}
                      onClick={() => {
                        setCurrentLanguage(lang);    // меняем текущий язык
                        setLanguageOpen(false);      // закрываем окно
                        // здесь можно добавить логику смены языка во всём приложении
                      }}
                      className="w-full text-left px-4 py-2 text-white hover:bg-purple-600/50 transition-colors duration-200 text-sm"
                    >
                      {lang.name}
                    </button>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      </header>

      {/* 
        ============================================================
        ОСНОВНОЙ КОНТЕНТ - секции для скролла
        Каждая секция занимает 100% высоты экрана (min-h-screen)
        ============================================================
      */}
      <main className="pt-20">  {/* pt-20 отступ сверху, чтобы контент не уходил под шапку */}
        {sections.map((section, index) => (
          <section
            key={section.id}
            id={section.id}
            className="relative min-h-screen flex items-center justify-center overflow-hidden border-b border-white/5"
          >
            {/* Фоновое изображение секции */}
            <div 
              className="absolute inset-0 z-0"
              style={{
                backgroundImage: `url(${section.image})`,
                backgroundSize: 'cover',
                backgroundPosition: '40% 58%',
                backgroundRepeat: 'no-repeat',
                backgroundAttachment: 'scroll'  // параллакс-эффект (фон не скроллится)
                // ← ИЗМЕНЯЙТЕ: 'fixed' на 'scroll' для обычного поведения
              }}
            />  
               
            {/* Тёмный градиент поверх фона для читаемости текста */}
            <div className="absolute inset-0 z-10 bg-gradient-to-b from-black/70 via-black/50 to-black/80"></div>
            {/* ← ИЗМЕНЯЙТЕ градиент: from-purple-900/70, to-black/90 и т.д. */}

            {/* Контент секции - центрирован */}
            <div className="relative z-20 text-center text-white px-6 max-w-4xl mx-auto">
              {/* Фото/изображение в центре */}
              {section.id === 'home' && (
                <div className="mb-8 animate-fadeInScale">
                  <img 
                    src={earthGif}
                    alt="Earth"
                    className="w-48 h-48 md:w-64 md:h-64 
                    rounded-full object-cover 
                    mx-auto shadow-2xl 
                    shadow-purple-900/50 
                    border-4 border-white/1" />
                    </div>
                  )}

              {/* Первая подпись (субтитул) */}
                           {/* Первая подпись (субтитул) - появляется с задержкой */}
              {textVisible && (
                <h2 className="text-3xl md:text-5xl font-bold mb-4 animate-fadeInUp">
                  {section.subtitle}
                </h2>
              )}

              {/* Вторая подпись (описание) - появляется с задержкой */}
              {textVisible && (
                <p className="text-lg md:text-xl text-gray-300 max-w-2xl mx-auto animate-fadeInUp animation-delay-200">
                  {section.description}
                </p>
                
              )}
                {/* БЛОК С КОМАНДОЙ - ПОЯВЛЯЕТСЯ ТОЛЬКО В СЕКЦИИ TEAM */}
{section.id === 'team' && (
  <div className="mt-12 text-left max-w-4xl mx-auto">
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
      <div className="bg-white/5 backdrop-blur-sm rounded-xl p-4 text-center">
        <div className="w-32 h-32 mx-auto rounded-full bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-4xl mb-3">📷</div>
        <h4 className="text-xl font-bold text-white">Prof. Dr. Yury A. Litvinov</h4>
        <p className="text-purple-300 text-sm">Principal Investigator</p>
      </div>
      <div className="bg-white/5 backdrop-blur-sm rounded-xl p-4 text-center">
        <div className="w-32 h-32 mx-auto rounded-full bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center text-4xl mb-3">📷</div>
        <h4 className="text-xl font-bold text-white">Dr. David Freire-Fernández</h4>
        <p className="text-purple-300 text-sm">Project: S+IMS</p>
      </div>
      <div className="bg-white/5 backdrop-blur-sm rounded-xl p-4 text-center">
        <div className="w-32 h-32 mx-auto rounded-full bg-gradient-to-br from-green-500 to-emerald-500 flex items-center justify-center text-4xl mb-3">📷</div>
        <h4 className="text-xl font-bold text-white">Dr. Jan Glorius</h4>
        <p className="text-purple-300 text-sm">Researcher</p>
      </div>
    </div>
    <div className="bg-white/5 backdrop-blur-sm rounded-xl p-6">
      <h4 className="text-xl font-bold text-white mb-4">Researchers</h4>
      <ul className="space-y-2 text-gray-300">
        <li>• Dr. David Freire-Fernández - Project: Schottky + Isochronous Mass Spectrometry (S+IMS)</li>
        <li>• Dr. Jan Glorius - Project: [to be added]</li>
        <li>• Dr. Dmytro Dmytriev - Project: [to be added]</li>
      </ul>
      <h4 className="text-xl font-bold text-white mt-6 mb-4">PhD Students</h4>
      <ul className="space-y-2 text-gray-300">
        <li>• Carlo Forconi - Project: [to be added]</li>
        <li>• Zac - Project: [to be added]</li>
      </ul>
      <h4 className="text-xl font-bold text-white mt-6 mb-4">Master & Bachelor Students</h4>
      <ul className="space-y-2 text-gray-300">
        <li>• [Name] - Data analysis</li>
      </ul>
    </div>
  </div>
)}
             
            </div>
          </section>
        ))}
      </main>

    </div>
  );
}

export default App;