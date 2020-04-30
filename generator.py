def generatohtml(name):
    from htmlparser import maine
    array = maine(name)

    htmlstring = """<!DOCTYPE html>
        <html>
        <head>
        <style>
        $baseColor: #398B93;
$borderRadius: 10px;
$imageBig: 100px;

$padding: 10px;

body {
   background-color: #483D8B;

}

.header {
   background-color: #00008B;
   color: white;
   font-size: 1.5em;
   padding: 1rem;
   text-align: center;
   text-transform: uppercase;
}

img {
   border-radius: 50%;
   height: 60px;
   width: 60px;
}

.table-users {
   border: ;
   border-radius: #000000;
   box-shadow: 3px 3px 0 rgba(0,0,0,0.1);
   max-width: calc(100% - 2em);
   margin: 1em auto;
   overflow: hidden;
   width: 80%;
}

table {
   width: 100%;

   td, th {
      color: darken($baseColor, 10%);
      padding: $padding;
   }

   td {
      text-align: center;
      vertical-align: middle;

      &:last-child {
         font-size: 0.95em;
         line-height: 1.4;
         text-align: left;
      }
   }

   th {
      background-color: lighten($baseColor, 50%);
      font-weight: 300;
   }

   tr {
      &:nth-child(2n) { background-color: blue; }
      &:nth-child(2n+1) { background-color: lighten($baseColor, 55%) }
   }
}

@media screen and (max-width: 700px) {
   table, tr, td { display: block; }

   td {
      &:first-child {
         position: absolute;
         top: 50%;
         transform: translateY(-50%);
         width: $imageBig;
      }

      &:not(:first-child) {
         clear: both;
         margin-left: $imageBig;
         padding: 4px 20px 4px 90px;
         position: relative;
         text-align: left;

         &:before {
            color: lighten($baseColor, 30%);
            content: '';
            display: block;
            left: 0;
            position: absolute;
         }
      }

      &:nth-child(2):before { content: 'Name:'; }
      &:nth-child(3):before { content: 'Email:'; }
      &:nth-child(4):before { content: 'Phone:'; }
      &:nth-child(5):before { content: 'Semester:'; }
      &:nth-child(6):before { content: 'Enroll no'; }
      &:nth-child(7):before { content: 'Reg no:'; }
      &:nth-child(8):before { content: 'Sec:'; }
      &:nth-child(9):before { content: 'Social Media:'; }

   }

   tr {
      padding: $padding 0;
      position: relative;
      &:first-child { display: none; }
   }
}

@media screen and (max-width: 500px) {
   .header {
      background-color: transparent;
      color: lighten($baseColor, 60%);
      font-size: 2em;
      font-weight: 700;
      padding: 0;
      text-shadow: 2px 2px 0 rgba(0,0,0,0.1);
   }

   img {
      border: 3px solid;
      border-color: lighten($baseColor, 50%);
      height: $imageBig;
      margin: 0.5rem 0;
      width: $imageBig;
   }

   td {
      &:first-child {
         background-color: lighten($baseColor, 45%);
         border-bottom: 1px solid lighten($baseColor, 30%);
         border-radius: $borderRadius $borderRadius 0 0;
         position: relative;
         top: 0;
         transform: translateY(0);
         width: 100%;
      }

      &:not(:first-child) {
         margin: 0;
         padding: 5px 1em;
         width: 100%;

         &:before {
            font-size: .8em;
            padding-top: 0.3em;
            position: relative;
         }
      }

      &:last-child  { padding-bottom: 1rem !important; }
   }

   tr {
      background-color: white !important;
      border: 1px solid lighten($baseColor, 20%);
      border-radius: $borderRadius;
      box-shadow: 2px 2px 0 rgba(0,0,0,0.1);
      margin: 0.5rem 0;
      padding: 0;
   }

   .table-users {
      border: none;
      box-shadow: none;
      overflow: visible;
   }
     }
        </style>
    </head>
    <body>


    <div class="table-users">
    <div class="header">RESULTS</div>

    <table cellspacing="0">
      <tr>
         <th>Picture</th>
         <th>NAME</th>
         <th>Email</th>
         <th>Phone</th>
         <th>SEMESTER</th>
         <th>ENROLL NO</th>
         <th>REG NO</th>
         <th>SEC</th>
         <th>Social Media</th>


       </tr>"""

    endstring = """</table>
               </div>

               </body>
                </html>"""

    def htmlgen(name='X', email='X', phone='X', semester='X', enroll='X', regno='X', sec='X', sm='X'):
        hmlsr = """<tr>
            <td><img src="https://st2.depositphotos.com/4264683/6406/v/950/depositphotos_64061101-stock-illustration-face-icon-with-shadow.jpg" alt="" /></td>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
            <td>{4}</td>
            <td>{5}</td>
            <td>{6}</td>
            <td>{7}</td>


             </tr>""".format(name, email, phone, semester, enroll, regno, sec, sm)

        return hmlsr

    stresult = ""

    for lis in array:
        result = htmlgen(lis[0], 'X', 'X', lis[1], lis[2], lis[3], lis[5], 'X')
        stresult += result
    instrumentality = htmlstring + stresult + endstring
    '''import os

    filepath = os.path.join('C:/Users/Shubhashish PC/PycharmProjects/trashproject/templates/', 'crap.html')
    if not os.path.exists('C:/Users/Shubhashish PC/PycharmProjects/trashproject/templates/'):
        os.makedirs('C:/Users/Shubhashish PC/PycharmProjects/trashproject/templates/')
    f = open(filepath, "w+")
    f.write(instrumentality)'''
    '''import os'''

    """if os.path.exists("/home/nitasearch/mysite/templates/crap.html"):
           os.remove("/home/nitasearch/mysite/templates/crap.html")"""

    #filepath = os.path.join('/home/nitasearch/mysite/templates', 'crap.html')

    f = open('/home/nitasearch/mysite/templates/crap.html', "w+")
    f.write(instrumentality)

    return instrumentality
