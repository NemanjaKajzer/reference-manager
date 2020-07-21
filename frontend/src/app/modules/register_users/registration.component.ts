import { Component, OnInit } from '@angular/core';
import { RegisterService } from '../../services/register.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {
  form: FormGroup;
  register;
  loading = false;
  submitted = false;

  constructor(private formBuilder: FormBuilder, private registerService: RegisterService) {

  }

  ngOnInit() {
    this.register = {
      username: '',
      password: '',
      email: '',
      first_name: '',
      last_name: ''
    };

    this.form = this.formBuilder.group({
      first_name: ['', [Validators.required, Validators.pattern('^[A-Z][a-z]+')]],
      last_name: ['', [Validators.required, Validators.pattern('^[A-Z][a-z]+')]],
      username: ['', [Validators.required, Validators.minLength(2), Validators.maxLength(12), Validators.pattern('^[A-Za-z0-9!@#$%^&*_|]{2,12}$')]],
      email: ['', [Validators.required, Validators.email, Validators.pattern('[a-zA-Z0-9]+@[a-zA-Z0-9]+.com')]],
      password: ['', [Validators.required, Validators.minLength(8), Validators.pattern('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')]]
    });
  }

  // ngOnInit() {
  //   this.forma = this.formBuilder.group({
  //     name: [''],
  //     surname: [''],
  //     username: [''],
  //     email: [''],
  //     password: [''],
  //     jmbg: [''],
  //     phoneNumber: ['']
  //   });
  // }

  get f() { return this.form.controls; }


  onSubmit() {
    this.submitted = true;

    this.loading = true;

    this.registerService.registerUser(this.register).subscribe(
      data => {
        console.log(data);
        alert('Success');
      },
      error => {
        alert('Error');
      }
    );
  }
}
