import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { AuthenticationService } from '../../services/authentication.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-login',
  templateUrl: './authentication.component.html',
  styleUrls: ['./authentication.component.css']
})
export class AuthenticationComponent implements OnInit {
  authentication;
  form: FormGroup;
  constructor(private authenticationService: AuthenticationService, private formBuilder: FormBuilder, private router: Router) {

  }

  ngOnInit() {
    this.authentication = {
      username: '',
      password: ''
    }
  }

  onSubmit() {


    this.authenticationService.login(this.authentication).subscribe(
      data => {
        console.log(data);


      },
      error => alert('Authentication failed')
    );

  }

}
