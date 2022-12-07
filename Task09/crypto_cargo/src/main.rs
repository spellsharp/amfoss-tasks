fn main() {
    let response = reqwest::blocking::get(
        "https://crypto.com/price"
    )
    .unwrap()
    .text()
    .unwrap();

    let document = scraper::Html::parse_document(&response);

    let title = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();

    let price = scraper::Selector::parse("div.css-b1ilzc").unwrap();

    let h24v = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    
    let change = scraper::Selector::parse("td.css-1b7j986>p").unwrap();

    let changes = document.select(&change).map(|x| x.inner_html());

    let titles = document.select(&title).map(|x| x.inner_html());

    let prices = document.select(&price).map(|x| x.inner_html());

    let common = document.select(&h24v).map(|x| x.inner_html());

    let mut titname: Vec<String> = vec![String::new(); 0];
    let mut cryprice: Vec<String> = vec![String::new(); 0];
    let mut changepri: Vec<String> = vec![String::new(); 0];
    let mut volume: Vec<String> = vec![String::new(); 0];
    let mut markcap: Vec<String> = vec![String::new(); 0];

   for i in titles{titname.push(i);}
   for i in prices{cryprice.push(i);}
   for i in changes{changepri.push(i);}

   let mut j=0;

   for i in common
   {
    if j%2==0
    {
        markcap.push(i);
    }
    else
    {
        volume.push(i);
    }
    j+=1;
   }

   let mut wtr=csv::Writer::from_path("cryptocargo.csv").unwrap();
   wtr.write_record(&["Name","Price","Change Rate", "24hr Hour volume", "Market Cap"]).unwrap();
   for i in 0..50
   {
   wtr.write_record([&titname[i],&cryprice[i],&changepri[i],&volume[i],&markcap[i]]);
   wtr.flush();
   }
   

}