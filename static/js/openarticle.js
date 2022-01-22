let article = document.getElementsByClassName('news_item');
let all_news = document.getElementsByClassName('news')[0];

for (let i = 0; article.length>=i;i++){
    article[i].onclick = function(event){
        let articletarget = article[i];

        //считывание текста статьи
        let name_article = articletarget.getElementsByClassName('text_name-item')[0].innerText;
        let desc_article = articletarget.getElementsByClassName('text_desc-item')[0].innerText;
        let date_article = articletarget.getElementsByClassName('text_date-item')[0].innerText;
        let img_article = articletarget.getElementsByClassName('news_item-img')[0].innerHTML;

        //закрытие блока всех новостей
        all_news.classList.toggle('display') ;

        //создание модального окна
        let modal_article = document.createElement('div');
        modal_article.classList.add('open_article');

        //создание кнопки "назад"
        let div_back_bth = document.createElement('div');
        div_back_bth.classList.add('open_article-back')

        let back_bth = document.createElement('button');
        back_bth.innerText = 'Back';
        div_back_bth.append(back_bth)

        modal_article.append(div_back_bth)
        back_bth.onclick = function(event){
            all_news.classList.toggle('display') ;
            modal_article.remove();
        }


        //создание блоков статьи в модальном окне
        let name_article_modal = document.createElement('div')
        name_article_modal.classList.add('open_article-name')
        name_article_modal.innerText = name_article;
        modal_article.append(name_article_modal)

        let div_desc = document.createElement('div');
        div_desc.classList.add('open_article-text')
        modal_article.append(div_desc)

        let image = document.createElement('div');
        image.classList.add('news_item-img')
        image.classList.add('open_article-img')
        image.innerHTML = img_article;
        div_desc.append(image)

        let desc_article_modal = document.createElement('div')
        desc_article_modal.classList.add('open_article-desc')
        desc_article_modal.innerText = desc_article;
        div_desc.append(desc_article_modal)

        let date_article_modal = document.createElement('div')
        date_article_modal.classList.add('open_article-date')
        date_article_modal.innerText = date_article;
        modal_article.append(date_article_modal)

        //запуск модального окна
        document.getElementsByClassName('container')[0].append(modal_article);
    }
}