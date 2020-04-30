def generatohtml(name):
    from htmlparser import maine
    array = maine(name)

    htmlstring = """<!DOCTYPE html>
      <html lang="en">
      <head>
         <meta charset="utf-8">
         <meta name="robots" content="noindex, nofollow">

          <title>SEARCH NITA</title>
              <meta name="viewport" content="width=device-width, initial-scale=1">
          <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
           <style type="text/css">
           /* FontAwesome for working BootSnippet :> */

          @import url('https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css');
         #team {
          background: #07051a !important;
        }

       .btn-primary:hover,
         .btn-primary:focus {
         background-color: #2F4F4F;
         border-color: #108d6f;
        box-shadow: none;
        outline: none;
       }

       .btn-primary {
         color: #fff;
         background-color: #2F4F4F;
          border-color: #007b5e;
       }

       section {
           padding: 60px 0;
        }

       section .section-title {
          text-align: center;
         color: #000000;
          margin-bottom: 50px;
        text-transform: uppercase;
        }

      #team .card {
      border: none;
      background: #000000;
       }

         .image-flip:hover .backside,
      .image-flip.hover .backside {
       -webkit-transform: rotateY(0deg);
      -moz-transform: rotateY(0deg);
       -o-transform: rotateY(0deg);
        -ms-transform: rotateY(0deg);
         transform: rotateY(0deg);
         border-radius: .25rem;
      }

       .image-flip:hover .frontside,
       .image-flip.hover .frontside {
        -webkit-transform: rotateY(180deg);
         -moz-transform: rotateY(180deg);
         -o-transform: rotateY(180deg);
           transform: rotateY(180deg);
          }

      .mainflip {
        -webkit-transition: 1s;
          -webkit-transform-style: preserve-3d;
         -ms-transition: 1s;
          -moz-transition: 1s;
         -moz-transform: perspective(1000px);
           -moz-transform-style: preserve-3d;
          -ms-transform-style: preserve-3d;
        transition: 1s;
           transform-style: preserve-3d;
          position: relative;
          }

        .frontside {
          position: relative;
         -webkit-transform: rotateY(0deg);
         -ms-transform: rotateY(0deg);
        z-index: 2;
        margin-bottom: 30px;
          }

      .backside {
        position: absolute;
        top: 0;
      left: 0;
      background: white;
       -webkit-transform: rotateY(-180deg);
      -moz-transform: rotateY(-180deg);
      -o-transform: rotateY(-180deg);
      -ms-transform: rotateY(-180deg);
       transform: rotateY(-180deg);
         -webkit-box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
       -moz-box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
       box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
       }

            .frontside,
            .backside {
                -webkit-backface-visibility: hidden;
                -moz-backface-visibility: hidden;
                -ms-backface-visibility: hidden;
                backface-visibility: hidden;
                -webkit-transition: 1s;
                -webkit-transform-style: preserve-3d;
                -moz-transition: 1s;
                -moz-transform-style: preserve-3d;
                -o-transition: 1s;
                -o-transform-style: preserve-3d;
                -ms-transition: 1s;
                -ms-transform-style: preserve-3d;
                transition: 1s;
                transform-style: preserve-3d;
            }

            .frontside .card,
            .backside .card {
                min-height: 30%;
            }

            .backside .card a {
                font-size: 18px;
                color: #ffffff !important;
            }

            .frontside .card .card-title,
            .backside .card .card-title {
                color: #ffffff !important;
            }

            .frontside .card .card-body img {
                width: 120px;
                height: 120px;
                border-radius: 50%;
            }    </style>
                <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
                <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
                <script type="text/javascript">
                    window.alert = function(){};
                    var defaultCSS = document.getElementById('bootstrap-css');
                    function changeCSS(css){
                        if(css) $('head > link').filter(':first').replaceWith('<link rel="stylesheet" href="'+ css +'" type="text/css" />');
                        else $('head > link').filter(':first').replaceWith(defaultCSS);
                    }
                    $( document ).ready(function() {
                      var iframe_height = parseInt($('html').height());
                      window.parent.postMessage( iframe_height, 'https://bootsnipp.com');
                    });
                   </script>
                   </head>
                  <body>
                  <!-- Team -->
                 <section id="team" class="pb-5">

                     <h5 class="section-title h1">RESULTS</h5>
                      <div class="row">"""


    endstring = """
                    </div>
                </div>
            </section>
            <!-- Team -->
            </body>
            </html>"""

    def htmlgen(name='X', email='X', phone='X', semester='X', enroll='X', regno='X', sec='X', sm='X'):
        hmlsr =""""<div class="col-xs-12 col-sm-6 col-md-4">
                <div class="image-flip" ontouchstart="this.classList.toggle('hover');">
                    <div class="mainflip">
                        <div class="frontside">
                            <div class="card">
                                <div class="card-body text-center">
                                    <p><img class=" img-fluid" src="https://st2.depositphotos.com/4264683/6406/v/950/depositphotos_64061101-stock-illustration-face-icon-with-shadow.jpg" alt="card image"></p>
                                    <h4 class="card-title">{0}</h4>
                                    <p style="font-family:Courier; color:White; ">Semester:{3}</p>
                                    <p style="font-family:Courier; color:White; ">Enroll No:{4}</p>
                                     <p style="font-family:Courier; color:White; ">Sec:{6}</p>

                                    <a href="#" class="btn btn-primary btn-sm"><i class="fa fa-plus"></i></a>
                                </div>
                            </div>
                        </div>
                        <div class="backside">
                            <div class="card">
                                <div class="card-body text-center mt-4">
                                    <h4 class="card-title">{0}</h4>
                                    <p style="font-family:Courier; color:White; ">Email:{2}</p>
                                    <p style="font-family:Courier; color:White; ">Phone:{2}</p>
                                     <p style="font-family:Courier; color:White; ">Reg no:{5}</p>
                                    <ul class="list-inline">
                                        <li class="list-inline-item">
                                            <a class="social-icon text-xs-center" target="_blank" href="https://www.facebook.com/search/top/?q={0}">
                                                <i class="fa fa-facebook"></i>
                                            </a>
                                        </li>



                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>""".format(name, email, phone, semester, enroll, regno, sec, sm)

        return hmlsr

    stresult = ""

    for lis in array:
        result = htmlgen(lis[0], 'X', 'X', lis[1], lis[2], lis[3], lis[5], 'X')
        stresult += result
    instrumentality = htmlstring + stresult + endstring
    import os

    if os.path.exists("/home/nitasearch/mysite/templates/crap.html"):
           os.remove("/home/nitasearch/mysite/templates/crap.html")

    filepath = os.path.join('/home/nitasearch/mysite/templates', 'crap.html')

    f = open(filepath, "w+")
    f.write(instrumentality)

    return instrumentality


#print(generatohtml('Shubhashish'))
