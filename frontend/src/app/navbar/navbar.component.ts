import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor(private router: Router) {

  }

  ngOnInit() {

  }

  showRegister() {
    this.router.navigate(['/registration']);
  }


  showLogin() {
    this.router.navigate(['/login']);
  }


  // showHomeAgent() {
  //   this.sessionService.report = false;
  //   this.sessionService.homeAgent = true;
  // }

  logOut() {

  }
}
