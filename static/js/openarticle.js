document.addEventListener('DOMContentLoaded', function () {
    let article = document.body.getElementsByClassName('news_item');
    let all_news = document.getElementsByClassName('news')[0];
    let selected_news = document.getElementsByName('nameArticle')[0];
    let div_addcom = document.getElementsByClassName('add_comm')[0];


    for (let i = 0; article.length > i; i++) {
        article[i].onclick = function (event) {
            let articletarget = article[i];
            if (event.target === document.getElementsByName('button'))
                alert();


            //считывание текста статьи
            let name_article = articletarget.getElementsByClassName('text_name-item')[0].innerText;
            let desc_article = articletarget.getElementsByClassName('text_desc-item')[0].innerText;
            let date_article = articletarget.getElementsByClassName('text_date-item')[0].innerText;
            let img_article = articletarget.getElementsByClassName('news_item-img')[0].innerHTML;
            let com_article = articletarget.getElementsByClassName('text_comments-item');

            //закрытие блока всех новостей
            all_news.classList.toggle('display');

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
            back_bth.onclick = function (event) {
                all_news.classList.toggle('display');
                div_addcom.classList.toggle('display')
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

            //открытие комментариев
            div_addcom.classList.toggle('display')
            //console.log((div_addcom))

            let com_article_modal = document.createElement('div')
            com_article_modal.classList.add('text_comments')
            com_article_modal.textContent = 'Комментарии:'
            for (item_com = 0; item_com<com_article.length; item_com++){

                let item_com_modal = document.createElement('div')
                item_com_modal.classList.add('text_comments-item')
                item_com_modal.innerHTML = com_article[item_com].innerHTML
                com_article_modal.append(item_com_modal)
            }
            modal_article.append(com_article_modal)


            //запуск модального окна
            document.getElementsByClassName('container')[0].prepend(modal_article);

            selected_news.options.selectedIndex = article[i].id;
            console.log(selected_news.options.selectedIndex)
        }
    }
})